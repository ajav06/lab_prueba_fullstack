import json

from flask_cors import cross_origin

from . import sets
from .repository import SetRepository

sets_repository = SetRepository()


@sets.route('/sets', methods=['GET'])
@cross_origin()
def fetch_all_sets():
    results = sets_repository.get_all()
    return {'results': [json.loads(i.to_json()) for i in results]}, 200


@sets.route('/sets/<id>', methods=['GET'])
@cross_origin()
def fetch_set_by_id(id: str):
    result = sets_repository.get_by_id(id)

    if not result:
        return {
            'message': f'Set with ID {id} does not exist.',
            'error_code': 'SET_NOT_FOUND',
        }, 404

    return {'results': json.loads(result.to_json())}, 200
