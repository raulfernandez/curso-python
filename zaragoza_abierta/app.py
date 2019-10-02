from zaragoza_abierta.utils import pretty_print, Colors as S, print_list
from zaragoza_abierta.equipamiento import get_equipments, get_equipment_categories, filter_equipments

"""
    # Zaragoza Abierta App

    Esta app es un ejercicio de la semana 3 dia 3.
"""


def main():
    equipamientos = get_equipments()
    categorias = get_equipment_categories(equipamientos)
    print_list(categorias, S.OKBLUE)
    filtered_equip = filter_equipments(equipamientos, 'Campos de Fútbol')
    print_list(filtered_equip)

if __name__ == "__main__":
    main()
