class Human:

    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def age_changer(self):
        self.age += 1
        return print(f'Today is your birthday! Now your age is {self.age}!')


person = Human('Ivan', 190, 80, 23)
person.age_changer()
