import json

from flask_cors import cross_origin

from . import cards
from .repository import CardRepository

cards_repository = CardRepository()


@cards.route('/cards', methods=['GET'])
@cross_origin()
def fetch_all_cards():
    results = cards_repository.get_all()
    return {'results': [json.loads(i.to_json()) for i in results]}, 200


@cards.route('/cards/<id>', methods=['GET'])
@cross_origin()
def fetch_card_by_id(id: str):
    result = cards_repository.get_by_id(id)

    if not result:
        return {
            'message': f'Card with ID {id} does not exist.',
            'error_code': 'CARD_NOT_FOUND',
        }, 404

    return {'results': json.loads(result.to_json())}, 200
