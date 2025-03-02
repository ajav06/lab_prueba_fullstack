import datetime
import json

from sqlalchemy import Column, Date, DateTime, Integer, String

from app.db import Base


class Set(Base):
    __tablename__ = 'set'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    series = Column(String, nullable=False)
    printed_total = Column(Integer)
    total = Column(Integer)
    ptcgo_code = Column(String)
    release_date = Column(Date)
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    symbol_url = Column(String)
    logo_url = Column(String)

    def __repr__(self):
        return f'<Set {self.name}>'

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'series': self.series,
            'printed_total': self.printed_total,
            'total': self.total,
            'ptcgo_code': self.ptcgo_code,
            'release_date': str(self.release_date),
            'updated_at': str(self.updated_at),
            'symbol_url': str(self.symbol_url),
            'logo_url': self.logo_url,
        }

    def to_json(self):
        return json.dumps(self.as_dict())
