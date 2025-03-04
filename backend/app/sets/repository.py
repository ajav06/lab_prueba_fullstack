from app.db import db

from .models import Set


class SetRepository:

    def get_all(self) -> list[Set]:
        """
         Summary
         -------
        Retrieves a list of all Set from the database

         Returns
         -------
         list[Set]
             Returns a list of all `Set` objects
        """
        return db.session.query(Set).all()

    def get_by_id(self, id: str) -> Set | None:
        """
        Summary
        -------
        Retrieves a Set from the database based on the provided id

        Parameters
        ----------
        id : str
            The unique identifier of a set

        Returns
        -------
        Set | None
            Returning a `Set` object or `None` if no set with the
            specified ID is found in the database
        """
        return db.session.query(Set).filter(Set.id == id).first()
