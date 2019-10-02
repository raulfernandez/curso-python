from utils import pretty_print, Colors as S, print_list
from equipamiento import get_equipments, get_equipment_categories, filter_equipments

import screens as s

"""
    # Zaragoza Abierta App

    Esta app es un ejercicio de la semana 3 dia 3.
"""
import sys


def main(*args):
    #
    #
    if len(args) == 1:
        s.main()
    elif len(args) == 2:
        if args[1] == 'c':
            equipamientos = get_equipments()
            categorias = get_equipment_categories(equipamientos)
            print_list(categorias)
        elif args[1] == 'e':
            equipamientos = get_equipments()
            print_list(equipamientos)
        else:
            s.command_help()
            exit(-1)

    elif len(args) == 3:
        if args[1] == 'f':
            equipamientos = get_equipments()
            equipamientos = filter_equipments(equipamientos, args[2])
            print_list(equipamientos)
        else:
            s.command_help()
            exit(-1)
    else:
        s.command_help()
        exit(-1)


if __name__ == "__main__":
    main(sys.argv)
