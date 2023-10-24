"""
OpenAI integration utilities.

Integration with OpenAI to generate 'flashcards' in csv form
based on course content
"""

import openai
from flashcards.settings.private import OPENAI_API_KEY  # pylint: disable=import-error,no-name-in-module

openai.api_key = OPENAI_API_KEY

def get_csv_from_openai():
    content_prompt = """
    The content for this course is the following

    What’s living in your food? Many of the foods that we consume daily owe their distinct characteristics
    and flavors to microbes, specifically through a biochemical process of fermentation (using bacteria,
    fungi, and other microorganisms to produce diverse foods). Gourmands and everyday consumers can
    quickly name some of the most popular fermented foods we consume—beer, yogurt, pickles—but, what
    about that coffee you drank this morning, or the chocolate bar you are saving for later?

    Through hands-on, at-home exercises, you will experiment with your food to grow your own microbial environments
    to make mead, sourdough, tempeh, and more—and discover the important role science plays in food
    fermentation. In Food Fermentation: The Science of Cooking with Microbes, you will explore the history
    of food and beverage fermentations and how it changes and enhances flavors, aromas, and tastes.
    You will engage with your peers in kitchen science, discussing how and why fermentation does or does
    not happen and what conditions you should consider to create the right growth opportunities.

    From chemistry to microbiology to your dinner plate, this course will analyze the role of microbes in production
    preservation, and enhancement of diverse foods across a variety of culinary traditions. You
    will study the following types of fermentations:@
    

    Lesson 1: Bread and Mead
    Lesson 2: Lactic Acid Bacteria
    Lesson 3: Beer and Sourdough
    Lesson 4: Wine and Vinegar
    Lesson 5: Filamentous Fungi
    Lesson 6: Aged Meat and Cheese
    Lesson 7: Chocolate and Coffee
    """  # noqa

    course_content = """
    ROBERTO KOLTER: While humans have been preparing and consuming
    microbial foods for thousands of years, it
    wasn't until relatively recent in history
    that humans first visualized individual microbes.
    The story of how this came to happen takes us back
    just a little over 300 years, to the mid-1600s, to the town of Delft
    in the Netherlands, beautifully drawn here in this painting
    by Johannes Vermeer.
    Amongst the Delft canals, there lived a contemporary
    of Vermeer, an enterprising textile merchant
    by the name of Antonie van Leeuwenhoek.
    He was driven by a great curiosity to explore the world around him.
    And as part of his trade, he wanted to be
    better able to assess the quality of the cloths he bought and sold.
    To achieve closer and closer inspection of the threads,
    van Leeuwenhoek learned the craft of lens grinding and polishing.
    He became quite good at it, eventually producing
    small spherical lenses that allowed magnifications never before
    accomplished by humans.
    He placed these lenses in rudimentary metal
    mounts, inventing the world's first microscopes.
    By placing samples in the pin-shaped holder
    and viewing them through his outstanding lenses,
    he was able to see dimensions no one had seen before.
    To his astonishment, he discovered tiny, little forms
    which, for the lack of better word, he called "little animals"
    or "animalcules."
    He noticed that they were of varied forms
    and remarkably numerous, writing in 1683, "All the people living in
    our united Netherlands are not as many as the living animals
    that I carry in my mouth this very day."
    Imagine if you will, that you are van Leeuwenhoek
    and are seeing through one of his microscopes at a single drop of water,
    collected from one of the canals of Delft.
    This is what you would have seen, a remarkable array of living entities.
    Some of the bigger ones are animals, indeed,
    such as the rotifer that is being tracked.
    But the smaller ones, swimming along rapidly, those are bacteria.
    And they're a few thousands of a millimeter,
    impossible to see with the naked eye.
    Yet these tiny microbes are responsible for all those wonderful fermentations
    that produce the beverages and foods we will be discussing in this course.
    It's truly a marvelous sight to behold the microbial activity that can
    be going on in a single drop of water.
    But van Leeuwenhoek's discovery would remain pretty much
    a curiosity for a couple of centuries.
    It was not until the second half of the 19th century
    that the French scientist Louis Pasteur came onto the scene
    and began to truly study the activities that were catalyzed
    by these tiniest of living creatures.
    Driven to solve practical problems, Pasteur
    became interested in studying wine production and the reasons
    why wine went bad.
    Being French, and wine being a key beverage in French culture,
    Pasteur knew there would be great interest in his studies on this topic.
    At the time, many people still believed that processes
    such as the turning of grape juice into wine happened spontaneously.
    This is a so-called theory of spontaneous generation of life.
    Simply by having liquids such as beef broth or grape juice in contact
    with air, microbes would be formed.
    Pasteur elegantly debunked that theory.
    First, he recognized that by heating such liquids,
    he could kill all the microbes present.
    In other words, he could sterilize the liquids.
    Then by making gooseneck flasks containing sterile medium,
    Pasteur was able to show that the medium would remain sterile,
    despite it's still having contact with the outside air.
    This ability to sterilize liquids allowed
    him to later on put into them new microbes and study their properties.
    We call this act of putting microbes into a growth medium inoculation.
    Having starting materials that are sterile or largely devoid of microbes
    can be a very useful practice when cooking with microbes,
    so do keep that in mind.
    Now, Pasteur had been trained as a chemist
    and was keenly interested in understanding
    the chemical transformations of matter that took place on Earth.
    One such transformation is the conversion of grape juice into wine.
    At the time, it was already known that the sugars in grape juice
    were converted to the gas carbon dioxide, or CO2, plus alcohol, ethanol,
    to be precise.
    But how this conversion was carried out was not known.
    Using his ability to sterilize liquids, Pasteur
    showed that he could inoculate sterile grape juice with a particular microbe
    and this would lead to the production of wine.
    He also was able to show that other microbes, when they contaminated
    the grape juice, were what caused the wine to go bad,
    for example, turn it into vinegar.
    The wine-making microbe was one that is going to become a close friend of ours
    in this course, the yeast Saccharomyces cerevisiae.
    Here, we see an image of this yeast, also known
    as baker's yeast or brewer's yeast.
    Yes, the same general microbe that makes wine
    is our friend that we use to make beer and bread,
    though there are subtle differences in the strains
    that we use to produce each of those [INAUDIBLE] foods,
    but we'll deal with that later.
    For now, let us simply appreciate the beauty of this microbe
    as we observe it magnified many thousands of times.
    Pasteur's discovery led to much better practices in wine-making,
    something the French, and the whole world
    for that matter, very much appreciated.
    It is still possible to go to restaurants in the French countryside
    and see these posters acknowledging the importance of Pasteur's work.
    Let me loosely translate the text around the image of Pasteur.
    "Give preferences to restaurants that include
    the wine in the price of the meal.
    Average of human life, 59 years for a water drinker,
    65 years for a wine drinker.
    87% of the centenarians are wine drinkers.
    Wine is the milk of all people."
    And last and most importantly, a quote directly from Pasteur,
    "Wine is the healthiest and most hygienic beverage."
    Now we know how we as humans first came to visualize microbes
    and first began to understand their role in making fermented foods.
    """

    # The prompt to ask ChatGPT to make anki cards.
    anki_prompt = """

    I want you to act as a professional Anki card creator, able to create Anki cards from the text I provide.

    Regarding the formulation of the card content, you stick to two principles:

    First, minimum information principle: The material you learn must be formulated in as simple way as it is only
    possible. Simplicity does not have to imply losing information and skipping the difficult part.
    Second, optimize wording: The wording of your items must be optimized to make sure that in minimum time the
    right bulb in your brain lights up. This will reduce error rates, increase specificity, reduce response time,
    and help your concentration.

    Please output these cards you create in a .csv format, with the questions and answers separated by commas.

    The following is a model card-create template for you to study.

    Text: The characteristics of the Dead Sea: Salt lake located on the border between Israel and Jordan.
    Its shoreline is the lowest point on the Earth's surface, averaging 396 m below sea level.
    It is 74 km long. It is seven times as salty (30% by volume) as the ocean.
    Its density keeps swimmers afloat.
    Only simple organisms can live in its saline waters.

    Where is the Dead Sea located?,On the border between Israel and Jordan
    What is the lowest point on the Earth's surface?,The Dead Sea shoreline
    What is the average level on which the Dead Sea is located?,400 meters (below sea level)
    How long is the Dead Sea?,70 km
    How much saltier is the Dead Sea as compared with the oceans?,7 times
    What is the volume content of salt in the Dead Sea?,30%
    Why can the Dead Sea keep swimmers afloat?,Due to high salt content
    Why is the Dead Sea called Dead?,Because only simple organisms can live in it
    Why only simple organisms can live in the Dead Sea?,Because of high salt content
    """  # noqa

    messages = [
        {"role": "system",
        "content": anki_prompt},
        {"role": "system",
        "content": content_prompt + course_content},
    ]

    if openai.api_key:
        c3 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=1.0,
        )
        # print(c3['choices'][0]['message']['content'])
        return c3['choices'][0]['message']['content']

        # c4 = openai.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=messages,
        #     temperature=1.0,
        # )

        # print(c4)
