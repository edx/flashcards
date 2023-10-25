"""
Implementation of AnkiConnect to create cards
"""
import genanki

from flashcards.apps.cards.cardgen import cards_from_block_id


def create_anki_cards(openai_data):
    """
    Generates anki cards from data
    """
    my_model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    my_deck = genanki.Deck(
        2059400111,
        'Demo Deck 1')

    rows = openai_data.split('\n')
    for row in rows:
        question, answer = row.split(',', 1)

        my_note = genanki.Note(
            model=my_model,
            fields=[question, answer])

        my_deck.add_note(my_note)

    genanki.Package(my_deck).write_to_file('demo_output.apkg')


def anki_from_block_id(course_id, block_id):
    csv_maybe = cards_from_block_id(course_id, block_id)
    result = csv_maybe.replace('\t', '')
    create_anki_cards(result)
    return csv_maybe  # return the CSV text so we can see it in testing
