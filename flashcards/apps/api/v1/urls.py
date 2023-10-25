""" API v1 URLs. """
from django.urls import path

from . import views

app_name = 'v1'
urlpatterns = [
    path('cards/<str:course_id>/<str:block_id>', views.cards, name='cards'),
]
