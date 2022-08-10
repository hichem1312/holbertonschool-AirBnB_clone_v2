#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    from models import storage_t

    if storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City')
    else:
        name = ""

        @property
        def cities(self):
            """Citties getter."""
            from models.city import City
            from models import storage
            cities = storage.all(City)
            list_city = []
            for i in cities:
                if cities[i].state_id == self.id:
                    list_city.append(cities[i])
            return list_city

    def __init__(self, *args, **kwargs):
        """Initialize model."""
        super().__init__(*args, **kwargs)
