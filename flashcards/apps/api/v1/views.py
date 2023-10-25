from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from flashcards.apps.cards.anki import anki_from_block_id


@api_view(['GET'])  # TODO get is completely wrong here but convenient for testing
@require_http_methods(['GET'])
def cards(request, course_id, block_id):
    cards = anki_from_block_id(course_id, block_id)
    return Response(cards)
