class Pet:
    legs = 4

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def voice(self):
        pass

    def how_many_legs(self):
        print(self.legs)


class Cat(Pet):

    def voice(self):
        print('Meowwww!')


class Parrot(Pet):
    legs = 2
    wing = 2

    def voice(self):
        print('Voice like human')

    def legs_count(self, count):
        if count == 1:
            print(self.legs)
        elif count == 2:
            print(super().legs)


cat = Cat('Markiz', 'male')
cat.voice()
parrot = Parrot('Kesha', 'male')
parrot.voice()
parrot.how_many_legs()
parrot.legs_count(1)
parrot.legs_count(2)
