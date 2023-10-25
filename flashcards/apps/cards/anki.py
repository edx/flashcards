"""
Implementation of AnkiConnect to create cards
"""
from flashcards.apps.cards.cardgen import cards_from_block_id
import json
import urllib.request
import requests
import genanki


def request(action, **params):
    """
    Helper function to make requests to Anki
    """
    return {'action': action, 'params': params, 'version': 6}


def invoke(action, **params):
    """
    Makes a request to Anki to interact with cards and decks.
    """
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    print("\n\nrequestJson:", requestJson)
    # response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
    response = requests.post('http://localhost:8765', data=requestJson)
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


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


def main():
    """
    Master function that gets a response from openai and passes the result to Anki
    """
    result = cards_from_block_id('course-v1:edX+DemoX+Demo_Course',
                                 'block-v1:edX+DemoX+Demo_Course+type@vertical+block@867dddb6f55d410caaa9c1eb9c6743ec')
    # TODO: Insert some kind of data validation here to make sure openai sent back something nice
    result = result.replace('\t', '')
    create_anki_cards(result)


main()
