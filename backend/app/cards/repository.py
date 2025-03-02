from app.db import db

from .models import Card


class CardRepository:
    def __init__(self):
        pass

    def get_all(self):
        return db.session.query(Card).all()

    def get_by_id(self, id: str) -> Card | None:
        return db.session.query(Card).filter(Card.id == id).first()

    def get_by_set_id(self, set_id: str):
        return db.session.query(Card).filter(Card.set_id == set_id).all()
