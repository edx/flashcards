"""
Implementation of AnkiConnect, which works super well :)
"""
import json
import urllib.request


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


# invoke('createDeck', deck='test1')
result = invoke('deckNames')
print('got list of decks: {}'.format(result))


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
