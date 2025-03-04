import datetime
import json

from sqlalchemy import ARRAY, Column, DateTime, Integer, String

from app.db import Base


class Card(Base):
    __tablename__ = 'card'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    supertype = Column(String, nullable=False)
    subtypes = Column(ARRAY(String))
    types = Column(ARRAY(String))
    set_id = Column(String, nullable=False)
    number = Column(String, nullable=False)
    rarity = Column(String)

    def __repr__(self):
        return f'<Card {self.name}>'

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'supertype': self.supertype,
            'subtypes': self.subtypes,
            'types': self.types,
            'set_id': self.set_id,
            'number': self.number,
            'rarity': self.rarity,
            'images': [i.as_dict() for i in self.images],
            'market': [i.as_dict() for i in self.market],
            'set': (
                set_data.as_dict()
                if hasattr(self, 'set') and (set_data := getattr(self, 'set'))
                else None
            ),
        }

    def to_json(self):
        return json.dumps(self.as_dict())


class Image(Base):
    __tablename__ = 'image'

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f'<Image {self.url}>'

    def as_dict(self):
        return {
            'id': self.id,
            'card_id': self.card_id,
            'url': self.url,
            'type': self.type,
        }

    def to_json(self):
        return json.dumps(self.as_dict())


class Market(Base):
    __tablename__ = 'market'

    id = Column(Integer, primary_key=True, index=True)
    card_id = Column(Integer, nullable=False)
    url = Column(Integer, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    market = Column(String, nullable=False)

    def __repr__(self):
        return f'<Market {self.market}>'

    def as_dict(self):
        return {
            'id': self.id,
            'card_id': self.card_id,
            'url': self.url,
            'updated_at': str(self.updated_at),
            'market': self.market,
        }

    def to_json(self):
        return json.dumps(self.as_dict())
