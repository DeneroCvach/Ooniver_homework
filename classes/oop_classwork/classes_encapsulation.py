from datetime import datetime


class Person:
    age: int
    name: str

    def __str__(self):
        return f'{self.age}, {self.__name}'

    def __init__(self, name, age=0):
        self.age = age
        self.__name = name

    def age_booster(self):
        today = datetime.now()
        if today.day == 19 and today.month == 6:
            self.age = self.age + 1


person = Person('denero', 22)
person_02 = Person('sashok', 22)
person.last_name = 'cvach'
person.age_booster()
age = person.age
print(person)
