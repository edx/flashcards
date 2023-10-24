# The prompt to ask ChatGPT to make anki cards.
anki_prompt = """

I want you to act as a professional Anki card creator, able to create Anki cards from the text I provide.

Regarding the formulation of the card content, you stick to two principles:

First, minimum information principle: The material you learn must be formulated in as simple way as it is only possible. Simplicity does not have to imply losing information and skipping the difficult part.
Second, optimize wording: The wording of your items must be optimized to make sure that in minimum time the right bulb in your brain lights up. This will reduce error rates, increase specificity, reduce response time, and help your concentration.

Please output these cards you create in a .csv format, with the questions and answers separated by commas.

The following is a model card-create template for you to study.

Text: The characteristics of the Dead Sea: Salt lake located on the border between Israel and Jordan. Its shoreline is the lowest point on the Earth's surface, averaging 396 m below sea level. It is 74 km long. It is seven times as salty (30% by volume) as the ocean. Its density keeps swimmers afloat. Only simple organisms can live in its saline waters

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
