class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'My name is {self.__name} {self.__surname}'

    def __len__(self):
        return self.__age

    def __del__(self):
        print('The person has been erased')


class Monster:
    def __init__(self, ugliness_level):
        self.__ugliness_level = ugliness_level


class Student(Person, Monster):
    def __init__(self, name, surname, age, level):
        super(Student, self).__init__(name=name, surname=surname, age=age)
        super(Student, self).__init__(ugliness_level=level)
        pass


def main():
    raul = Student('Raul', 'Fernandez', 36, 999)
    print(raul, len(raul))
    del raul
