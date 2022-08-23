#TODO Run pylint on this code. Fix all the problems until you get a score of 10.
import logging
from datetime import date, datetime
today = date.today()
class Person:
    """a person with a name and a birthday
    Example:
    >>> p = Person("Hacker")
    >>> p.name
    'Hacker'
    >>> p.age
    0
    >>> p.set_birthday(2001, 1, 1)
    >>> p.age
    20
    >>> str(p)
    'young adult named Hacker'
    >>> p.set_birthday(2001,12,31)
    >>> p.age
    19
    >>> str(p)
    'teenager named Hacker'
    """

    def __init__(self, name, birthday=date.today()):
        if not isinstance(name,str):
            raise TypeError("name must be a string")
        self._name = name
        self.birthday = birthday

    @staticmethod
    def youthfulness(p):
        """Comment based on a person's age"""

        if p.age < 0: return "unborn"
        elif p.age < 1: return "baby"
        elif p.age < 6: return "child"
        elif p.age < 13: return "youth"
        elif p.age < 20: return "teenager"
        elif p.age < 30: return "young adult"
        elif p.age < 60: return "middle-ager"
        elif p.age < 80: return "senior"
        elif p.age < 90: return "octogenarian"  # someone 80-89
        elif p.age < 90: return "nonagenarian"  # someone 90-99
        else:
            return "centenarian"            # someone >= 100, aka "centarian"
    
    def __str__(self):
        return Person.youthfulness(self)+ " named " + self._name

    def set_birthday(self, year: int, month: int, day: int):
        self.birthday = date(year, month, day)

    @property
    def age(self) -> int:
        b = self.birthday
        age = today.year - b.year
        if (b.month,b.day) > (today.month,today.day):
            # this year's birthday has not occurred yet
            age -= 1
        return age

    @property
    def name(self) -> str:
        return self._name

    def __eq__(self, o):
        """Two people are considered to be equal if they have the same name and the same birthday"""
        if not isinstance(o, Person):
            return False
        else:
            return self._name == o._name and self.birthday == o.birthday
