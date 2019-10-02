import utils as u


def main():
    u.pretty_print('Zaragoza Abierta command usage', u.Colors.HEADER)
    u.pretty_print('---------------------------------------------------------')
    u.pretty_print('> zabapp c                 List of equipment categories')
    u.pretty_print('> zabapp e                 List of equipments')
    u.pretty_print('> zabapp f "Category 1"    Filter equipments by category')
    u.pretty_print('> zabapp h                 Show help')


def command_help():
    u.pretty_print('Help zabapp', u.Colors.HEADER)
    u.pretty_print('zabapp [c|e|f "filter"]')
