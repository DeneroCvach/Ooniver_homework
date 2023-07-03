class Human:

    def __init__(self, name, height, weight, age, salary=1000):
        self.name = name
        self.height = height
        self.weight = weight
        self.__age = age
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, premium):
        self.__salary += premium

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            print("age can't be negative")
        else:
            self.__age = age
            return self.__age


person = Human('Ivan', 190, 80, 23)
print(person.salary)
person.salary = 500
print(person.salary)
print(person.get_age())
person.set_age(-1)
print(person.set_age(30))
