FROM ubuntu:focal as base

# Packages installed:

# language-pack-en locales; ubuntu locale support so that system utilities have a consistent
# language and time zone.

# python3.9; version of python compatible with Anki

# libmysqlclient-dev; to install header files needed to use native C implementation for
# MySQL-python for performance gains.

# libssl-dev; # mysqlclient wont install without this.

# make; needed to build the gevent wheel (unclear why a binary wheel isn't being found and used)

# python3.9-dev; to install header files for python extensions; much wheel-building depends on this

# python3.9-venv; install Python 3.9 version of venv for creating a virtualenv with pip

# gcc; for compiling python extensions distributed with python packages like mysql-client

# unzip; for extracting the downloaded watchman binary release

# wget; for fetching a local copy of common_constraints.txt to edit until the Django 4.2 upgrade is complete

# If you add a package here please include a comment above describing what it is used for
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy install --no-install-recommends software-properties-common && \
    apt-add-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -qy install --no-install-recommends \
    language-pack-en \
    locales \
    make \
    python3.9 \
    python3.9-dev \
    python3.9-venv \
    # The mysqlclient Python package has install-time dependencies
    libmysqlclient-dev \
    libssl-dev \
    pkg-config \
    gcc \
    unzip \
    wget && \
    rm -rf /var/lib/apt/lists/*

# Create Python env
ENV VIRTUAL_ENV=/edx/app/venvs/flashcards
RUN python3.9 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DJANGO_SETTINGS_MODULE flashcards.settings.production

EXPOSE 8491
RUN useradd -m --shell /bin/false app

WORKDIR /edx/app/flashcards

# Copy the requirements explicitly even though we copy everything below
# this prevents the image cache from busting unless the dependencies have changed.
COPY requirements/pip.txt /edx/app/flashcards/requirements/pip.txt
COPY requirements/production.txt /edx/app/flashcards/requirements/production.txt

# Dependencies are installed as root so they cannot be modified by the application user.

RUN pip install --no-cache-dir -r requirements/pip.txt
RUN pip install --no-cache-dir -r requirements/production.txt

RUN mkdir -p /edx/var/log

# Code is owned by root so it cannot be modified by the application user.
# So we copy it before changing users.
USER app

# Gunicorn 19 does not log to stdout or stderr by default. Once we are past gunicorn 19, the logging to STDOUT need not be specified.
CMD gunicorn --workers=2 --name flashcards -c /edx/app/flashcards/flashcards/docker_gunicorn_configuration.py --log-file - --max-requests=1000 flashcards.wsgi:application

# This line is after the requirements so that changes to the code will not
# bust the image cache
COPY . /edx/app/flashcards

# We don't switch back to the app user for devstack because we need devstack users to be
# able to update requirements and generally run things as root.
FROM base as dev
USER root
ENV DJANGO_SETTINGS_MODULE flashcards.settings.devstack

# Install watchman
RUN wget https://github.com/facebook/watchman/releases/download/v2023.10.23.00/watchman-v2023.10.23.00-linux.zip
RUN unzip watchman-v2023.10.23.00-linux.zip
RUN mkdir -p /usr/local/{bin,lib} /usr/local/var/run/watchman
RUN cp watchman-v2023.10.23.00-linux/bin/* /usr/local/bin
RUN cp watchman-v2023.10.23.00-linux/lib/* /usr/local/lib
RUN chmod 755 /usr/local/bin/watchman
RUN chmod 2777 /usr/local/var/run/watchman

RUN pip install --no-cache-dir -r /edx/app/flashcards/requirements/dev.txt

CMD while true; do python ./manage.py runserver 0.0.0.0:8491; sleep 2; done
