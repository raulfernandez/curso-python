import re


def regex_exercise1():
    frase = 'CTA es un centro de enseñanza de tecnologia situado en la ciudad de Zaragoza'
    matches = re.findall(r'cen\w+', frase, re.IGNORECASE)
    print('Matches:', matches)


def bitwise_exercise1():
    valor = 10
    valor_binario = bin(10)
    print(valor, valor_binario, bin(valor << 1), bin(valor >> 1), bin(valor & 10), bin(valor | 10), bin(valor ^ 10))


def sumar(a, b):
    """
    Function que devuelve la suma de a y b

    >>> sumar(5, 5)
    10
    >>> sumar(5, 5)
    2

    """
    return a + b


def main():
    # regex_exercise1()
    # bitwise_exercise1()
    pass