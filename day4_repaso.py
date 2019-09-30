from functools import reduce


def repaso():
    # parte funcional
    # map, reduce, filter
    my_list = list(range(10))
    print(my_list)

    my_mapped_list = map(lambda item: item ** 2, my_list)
    print(my_mapped_list)

    my_reduce_result = reduce(lambda acc, val: acc + val, my_list)
    print(my_reduce_result)

    my_filter_list = filter(lambda item: item % 2 == 0, my_list)
    print(my_filter_list)

    pass


# map
def quitar_vocales(palabra: str):
    nueva_palabra = ''
    vocales = ['a', 'e', 'i', 'o', 'u']
    for caracter in palabra:
        if caracter.lower() not in vocales:
            nueva_palabra += caracter
    return nueva_palabra


def quitar_vocales2(palabra: str):
    vocales = ['a', 'e', 'i', 'o', 'u']
    nueva_palabra = ''.join([caracter for caracter in palabra if caracter.lower() not in vocales])
    return nueva_palabra


def repaso_ejercicio():
    # Devolver palabras sin las vocales
    palabras = ['Hola', 'Adios', 'Mundo', 'Python']
    # mis_nuevas_palabras = list(map(quitar_vocales, palabras))
    mis_nuevas_palabras = list(map(quitar_vocales2, palabras))
    print(mis_nuevas_palabras)


# filter
def repaso_filtros():
    lista_numeros = range(-10, 10)
    lista_positivos = filter(lambda x: x < 0, lista_numeros)
    print(list(lista_positivos))


# reduce
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def repaso_reduce():
    lista = [character for character in char_range('a', 'z')]
    nueva_lista = reduce(lambda acc, val: acc + val, lista, '')
    print(nueva_lista)


def main():
    """
    # Day 4 - Week 1 - Python

    Para hoy:
    * Repaso 💩
    * Trabajo con ficheros
    * POO
    * netacad
    * applicacion practica
    """
    repaso_reduce()

    pass
