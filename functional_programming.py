# map, filter, reduce

def exercise1():
    palabras = list()
    palabras.append('Hola')
    palabras.append('Sola')
    palabras.append('Mola')
    palabras.append('Sala')

    palabras2 = [palabra for palabra in palabras if palabra.lower().startswith('s')]
    print(palabras2)


def main():
    # exercise1();
    print(list(filter(lambda x: x % 2 != 0, range(100))))
    print(list(map(lambda x: x - 1, range(200))))


if __name__ == "__main__":
    main()
