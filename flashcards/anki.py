"""
Implementation of AnkiConnect, which works super well :)
"""
import json
import urllib.request
from flashcards.utils import get_csv_from_openai

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
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
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
    result = invoke('deckNames')
    print('got list of decks: {}'.format(result))

    # csv = """What is food fermentation?,A biochemical process using microorganisms to produce diverse foods
    # What are some examples of popular fermented foods?,Beer, yogurt, pickles
    # What foods can you create with microbial environments?,Mead, sourdough, tempeh, and more
    # What is the purpose of this course?,To explore the role of microbes in food fermentation
    # What will you study in this course?,Different types of fermentations"""

    rows = openai_data.split('\n')
    for row in rows:
        question, answer = row.split(',', 1)
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
        print('\nAdding card:', note)
        invoke('addNote', note=note)

def main():
    result = get_csv_from_openai()
    # TODO: Insert some kind of data validation here to make sure openai sent back something nice

    result = result.replace('\t','')
    # print(result)
    create_anki_cards(result)

main()
# invoke('createDeck', deck='test1')





# Below is some code using just the plain ol' anki package, which failed to work on my machine.

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
