from Plataforma.Usuario import Usuario
from typing import List


def procesar():
    return iter([par for par in range(100) if par % 2 == 0])


class Coche:
    pass


def main():
    # gen = procesar()
    # print(next(gen))
    # print(next(gen))
    # print(next(filter(lambda x: x > 20, [par for par in range(100) if par % 2 == 0])))
    usr = Usuario('jsmith', 'John', 'Smith')
    print(usr.serializar())
