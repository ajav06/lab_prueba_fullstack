from app.db import db

from .models import Card, Image, Market


class ImageRepository:

    def get_all(self) -> list[Image]:
        return db.session.query(Image).all()

    def get_by_id(self, id: str) -> Image | None:
        return db.session.query(Image).filter(Image.id == id).first()

    def get_by_card_id(self, card_id: str) -> list[Image]:
        return db.session.query(Image).filter(Image.card_id == card_id).all()


class MarketRepository:

    def get_all(self) -> list[Market]:
        return db.session.query(Market).all()

    def get_by_id(self, id: str) -> Market | None:
        return db.session.query(Market).filter(Market.id == id).first()

    def get_by_card_id(self, card_id: str) -> list[Market]:
        return db.session.query(Market).filter(Market.card_id == card_id).all()


class CardRepository:
    image_repository = ImageRepository()
    market_repository = MarketRepository()

    def get_all(self) -> list[Card]:
        return db.session.query(Card).all()

    def get_by_id(self, id: str) -> Card | None:
        card = db.session.query(Card).filter(Card.id == id).first()

        if not card:
            return None

        card.images = self.image_repository.get_by_card_id(id)
        card.market = self.market_repository.get_by_card_id(id)
        return card

    def get_by_set_id(self, set_id: str) -> list[Card]:
        cards = db.session.query(Card).filter(Card.set_id == set_id).all()

        for card in cards:
            card.images = self.image_repository.get_by_card_id(card.id)
            card.market = self.market_repository.get_by_card_id(card.id)

        return cards
