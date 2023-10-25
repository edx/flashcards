"""
Implementation of AnkiConnect to create cards
"""
from flashcards.apps.cards.cardgen import cards_from_block_id
import json
import urllib.request
import requests


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
    rows = openai_data.split('\n')
    for row in rows:
        question, answer = row.split(',', 1)
        print(question,'\\n',answer)
        note = {
            "deckName": "test1",
            "modelName": "Basic",
            "fields": {
                "Front": question,
                "Back": answer,
            },
            # "tags": [ # leaving this out for now, not needed for mvp
            #     "yomichan"
            # ],
        }
        invoke('addNote', note=note)


def main():
    """
    Master function that gets a response from openai and passes the result to Anki
    """
    # 'block-v1:edX+DemoX+Demo_Course+type@sequential+block@19a30717eff543078a5d94ae9d6c18a5/'
    # 'block-v1:edX+DemoX+Demo_Course+type@vertical+block@867dddb6f55d410caaa9c1eb9c6743ec'
    result = cards_from_block_id('course-v1:edX+DemoX+Demo_Course',
                                 'block-v1:edX+DemoX+Demo_Course+type@vertical+block@867dddb6f55d410caaa9c1eb9c6743ec')
    # TODO: Insert some kind of data validation here to make sure openai sent back something nice
    result = result.replace('\t', '')
    create_anki_cards(result)


main()


# Below is some code using just the plain ol' anki package, which has failed to work on my machine so far.

# import anki
# # from anki.collection import ImportCsvRequest
# import aqt

# class API:
#   def __init__(self):
#     self.window = aqt.mw
# # deck = mw.col.decks.get_deck(0)
# # print(deck)

# api = API
# print(api)
