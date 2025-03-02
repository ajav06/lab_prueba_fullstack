import json

from sqlalchemy import ARRAY, Column, Integer, String

from app.db import Base


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True)
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
        }

    def to_json(self):
        return json.dumps(self.as_dict())
