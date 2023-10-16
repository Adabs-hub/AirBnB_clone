#!/usr/bin/python3
"""City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id : The state id.(str).
        name : The name of the city(str).
    """

    state_id = ""
    name = ""
