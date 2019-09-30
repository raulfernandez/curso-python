import math


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('A person is born')


class Robot:
    def __init__(self, batery, os):
        self.batery = batery
        self.os = os
        print('A robot is assembled')


class Cyborg(Person, Robot):
    def __init__(self, name, age, batery, os):
        Person.__init__(self, name, age)
        Robot.__init__(self, batery, os)


class A:
    pass

class B(A):
    pass

class C(B):
    pass


def main():
    print(dir(math))
