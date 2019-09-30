import threading
import time


class Waiter:
    def __init__(self, name: str, age: int, experience: float):
        self.__name = name
        self.__age = age
        self.__xp = experience
        self.__busy = False

    @property
    def name(self):
        return self.__name

    @property
    def is_busy(self):
        return self.__busy

    def serve_drinks(self):
        print(f'{self.name} is serving drinks...')
        self.__busy = True
        time.sleep(10)
        self.__busy = False

    def __str__(self):
        return f'Waiter: {self.name}'


class Bar:
    def __init__(self, name: str, waiters: list = None):
        self.__name = name
        self.__waiters = waiters if waiters is not None else list()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def staff(self):
        return self.__waiters

    def get_name(self) -> str:
        return self.__name

    def hire_waiter(self, waiter: Waiter):
        if waiter is not None and isinstance(waiter, Waiter):
            self.__waiters.append(waiter)

    def help_customer(self, waiter_name):
        orders = []
        available_waiter = list(filter(lambda waiter: waiter.name == waiter_name, self.__waiters))

        if len(available_waiter) != 0:
            available_waiter = available_waiter[0]
            if not available_waiter.is_busy:
                order = threading.Thread(target=available_waiter.serve_drinks)
                orders.append(order)
                order.start()
            else:
                print('\nThe waiter is busy at the moment. Try later')
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'{self.__name} has {len(self.__waiters)} waiters'


def main():
    """
    # Day 4 - Week 1 - Python

    Para hoy:
    * Repaso 💩
    * Trabajo con ficheros 💩
    * POO 💩
    * netacad 💩
    * applicacion practica 💩
    """
    bar_manolo = Bar('Manolo\'s Irish Tabern')

    bar_manolo.hire_waiter(Waiter('John Smith', 36, 12))
    bar_manolo.hire_waiter(Waiter('Mary Poppins', 25, 3))

    print(bar_manolo)

    bar_open = True
    while bar_open:
        waiter_name = input('Choose your waiter: ')
        bar_open = bar_manolo.help_customer(waiter_name)

