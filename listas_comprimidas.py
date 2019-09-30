from typing import Callable


def to_power_three(number):
    """
    Returns the number to the power of three.
    :param number: The number
    :return: The number to the power of three
    """
    return number ** 3


def suma(a: int, b: int) -> int:
    print(a + b)


def process(number: int, fn: Callable[[int], int]) -> int:
    return fn(number)


def exercise1():
    print([(lambda x: x+1)(number) for number in range(20) if number % 2 == 0])


def main():
    my_range = range(20)
    my_odd_list = list(filter(lambda number: (number % 2 == 0), my_range))
    my_other_odd_list = [to_power_three(number) for number in my_range if number % 2 == 0]

    print(my_odd_list, my_other_odd_list, sep='\n')

    #########
    items1 = [1, 2, 3, 4, 5]
    items2 = ['a', 'b', 'c', 'd', 'f']
    fusion = list(zip(items1, items2))
    print(fusion)

    ##########
    suma(1, 3.1)
    resta = lambda a, b: a-b
    print(type(resta), resta(3, 2))

    ##########
    result = process(10, lambda x: x**2)
    print(result)

    ##########
    exercise1()

if __name__ == "__main__":
    main()
