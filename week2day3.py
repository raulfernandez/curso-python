from enum import Enum
from collections import Counter
import random


class CajaBombones:
    def __init__(self):
        self.__bombones = ['a', 'b', 'c', 'd', 'e']
        self.__indice = 0

    def __iter__(self):
        # for bombon in self.__bombones:
        #     yield bombon
        self.__indice = 0
        return self

    def __next__(self):
        if self.__indice < len(self.__bombones):
            bombon = self.__bombones[self.__indice]
            self.__indice += 1
            return bombon
        else:
            raise StopIteration

    def __len__(self):
        return len(self.__bombones)


class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __eq__(self, other):
        return self.__name == other.name


class PuntosCardinales(Enum):
    Norte = 1
    Sur = 2
    Este = 3
    Oeste = 4


def main():
    # print(PuntosCardinales.Norte.name == 'Norte')
    # print(PuntosCardinales.Norte.value == 1)
    items = random.randrange(0, 10, 1)
    Counter(items).most_common(1)