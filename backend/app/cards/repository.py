from app.db import db
from app.sets.repository import SetRepository

from .models import Card, Image, Market


class ImageRepository:

    def get_all(self) -> list[Image]:
        """
        Summary
        -------
        Retrieves a list of all Image from the database

        Returns
        -------
        list[Image]
            Returns a list of all `Image` objects
        """
        return db.session.query(Image).all()

    def get_by_id(self, id: str) -> Image | None:
        """
        Summary
        -------
        Retrieves an Image from the database based on the provided id

        Parameters
        ----------
        id : str
            The unique identifier of an image

        Returns
        -------
        Image | None
            Returning an `Image` object or `None` if no image with the
            specified ID is found in the database
        """
        return db.session.query(Image).filter(Image.id == id).first()

    def get_by_card_id(self, card_id: str) -> list[Image]:
        """
        Summary
        -------
        Retrieves a list of Image based on a given card_id.

        Parameters
        ----------
        card_id : str
            The unique identifier of a card

        Returns
        -------
        list[Image]
            Returning a list of `Image` object that have the
            specified card_id
        """
        return db.session.query(Image).filter(Image.card_id == card_id).all()


class MarketRepository:

    def get_all(self) -> list[Market]:
        """
        Summary
        -------
        Retrieves a list of all Market from the database

        Returns
        -------
        list[Market]
            Returns a list of all `Market` objects
        """
        return db.session.query(Market).all()

    def get_by_id(self, id: str) -> Market | None:
        """
        Summary
        -------
        Retrieves a Market from the database based on the provided id

        Parameters
        ----------
        id : str
            The unique identifier of a market

        Returns
        -------
        Market | None
            Returning a `Market` object or `None` if no market with the
            specified ID is found in the database
        """
        return db.session.query(Market).filter(Market.id == id).first()

    def get_by_card_id(self, card_id: str) -> list[Market]:
        """
        Summary
        -------
        Retrieves a list of Market based on a given card_id.

        Parameters
        ----------
        card_id : str
            The unique identifier of a card

        Returns
        -------
        list[Market]
            Returning a list of `Market` object that have the
            specified card_id
        """
        return db.session.query(Market).filter(Market.card_id == card_id).all()


class CardRepository:
    image_repository = ImageRepository()
    market_repository = MarketRepository()
    set_repository = SetRepository()

    def get_all(self) -> list[Card]:
        """
         Summary
         -------
        Retrieves a list of all Card from the database

         Returns
         -------
         list[Card]
             Returns a list of all `Card` objects
        """
        return db.session.query(Card).all()

    def get_by_id(self, id: str) -> Card | None:
        """
        Summary
        -------
        Retrieves a card from the database based on the provided id and
        fetches related images, market data, and set information

        Parameters
        ----------
        id : str
            The unique identifier of a card

        Returns
        -------
        Card | None
            Returning a `Card` object or `None` if no card with the
            specified ID is found in the database
        """
        card = db.session.query(Card).filter(Card.id == id).first()

        if not card:
            return None

        card.images = self.image_repository.get_by_card_id(id)
        card.market = self.market_repository.get_by_card_id(id)
        card.set = self.set_repository.get_by_id(card.set_id)
        return card

    def get_by_set_id(self, set_id: str) -> list[Card]:
        """
        Summary
        -------
        Retrieves a list of cards by a specified set ID and populates each card with images
        and market data

        Parameters
        ----------
        set_id : str
            The unique identifier of a set

        Returns
        -------
        list[Card]
            Returning a list of `Card` objects that belong to the set with the specified set_id.
        """
        cards = db.session.query(Card).filter(Card.set_id == set_id).all()

        for card in cards:
            card.images = self.image_repository.get_by_card_id(card.id)
            card.market = self.market_repository.get_by_card_id(card.id)

        return cards
