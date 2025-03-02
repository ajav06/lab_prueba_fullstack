from app.db import db

from .models import Set


class SetRepository:

    def get_all(self):
        return db.session.query(Set).all()

    def get_by_id(self, id: str) -> Set | None:
        return db.session.query(Set).filter(Set.id == id).first()
