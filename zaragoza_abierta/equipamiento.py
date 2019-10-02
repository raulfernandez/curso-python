"""
    Modulo de operaciones sobre equipamientos
"""

import requests
import snakecase
import json


class Equipment:
    def __init__(self):
        self.same_as = None
        self.id = None
        self.title = None
        self.servicios = None
        self.last_updated = None
        self.category = None
        self.institucion = None
        self.tipo_entidad = None
        self.portal = None
        self.calle = None
        self.geometry = None
        self.type = None

    def load(self, data):
        snake_data = {snakecase.convert(key): value for key, value in data}
        self.__dict__ = json.loads(snake_data)


def get_equipments():
    data = requests.request('GET', 'http://www.zaragoza.es/sede/servicio/equipamiento/catalog.json?rows=50&start=50')
    return data.json()['result']


def get_equipment_categories(equipments: list):
    # From a list of equipments, extract the categories in a dict, so we don't repeat categories, then sort them
    return sorted([cat for cat in {e['category'][0]['title'] for e in equipments if e.get('category') is not None}])


def _has_category(equipment: dict, category: str):
    categories = equipment.get('category')
    return categories and categories[0]['title'].lower() == category.lower()


def filter_equipments(equipments: list, category: str):
    return filter(lambda e: _has_category(e, category), equipments)
