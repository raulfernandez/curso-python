"""
    Modulo de operaciones sobre equipamientos
"""

import requests


def get_equipments():
    data = requests.request('GET', 'http://www.zaragoza.es/sede/servicio/equipamiento/catalog.json?rows=50&start=50')
    return data.json()['result']


def get_equipment_categories(equipments: list):
    return sorted([cat for cat in {e['category'][0]['title'] for e in equipments if e.get('category') is not None}])


def _has_category(equipment: dict, category: str):
    categories = equipment.get('category')
    return categories and categories[0]['title'].lower() == category.lower()


def filter_equipments(equipments: list, category: str):
    return filter(lambda e: _has_category(e, category), equipments)
