from abc import ABC


class Mouse:
    def run(self):
        print('Ok, i am running!')


class Chipmunk:
    def run(self):
        print('Ok, i am running!')

    def jump(self):
        print('Ok, i will try to jump!')


class Fly:
    def fly(self):
        print('Now i am flying!')


class Rescuers(ABC):
    def __init__(self, name, weight, height, tiredness=0):
        self.name = name
        self.weight = weight
        self.height = height
        self.tiredness = tiredness

    def change_weight(self, changes=None):
        if changes is None:
            changes = 0.01
        self.weight += min(changes, 0.05)

    def rest(self):
        print(f'{self.name} need to rest..')
        self.tiredness *= 0


class Chip(Chipmunk, Rescuers):
    def __init__(self):
        super().__init__('Chip', 0.02, 5, 9)

    def run(self):
        print('Ok, i am running!')
        self.tiredness += 1
        if self.tiredness >= 10:
            self.rest()

    def jump(self):
        print('Ok, i will try to jump!')
        self.tiredness += 1
        if self.tiredness >= 10:
            self.rest()


class Dale(Chipmunk, Rescuers):
    def __init__(self):
        super().__init__('Dale', 0.03, 6)

    def run(self):
        print('Ok, i am running!')
        self.tiredness += 1
        if self.tiredness >= 10:
            self.rest()

    def jump(self):
        print('Ok, i will try to jump!')
        self.tiredness += 1
        if self.tiredness >= 10:
            self.rest()


class Rocky(Mouse, Rescuers):
    def __init__(self):
        super().__init__('Rocky', 0.05, 7)

    def run(self):
        print('Ok, i am running!')
        self.tiredness += 1
        if self.tiredness >= 10:
            self.rest()


class Gadget(Mouse, Rescuers):
    def __init__(self):
        super().__init__('Gadget', 0.03, 5)

    def run(self):
        print('Ok, i am running!')
        self.tiredness += 1
        if self.tiredness >= 10:
            self.rest()


class Zipper(Fly, Rescuers):
    def __init__(self):
        super().__init__('Zipper', 0.01, 2)

    def fly(self):
        print('Now i am flying!')
        self.tiredness += 1
        if self.tiredness >= 10:
            self.rest()

    def change_weight(self, changes=None):
        if changes is None:
            changes = 0.001
        try:
            if self.weight + changes > 0.02:
                raise ValueError("Zipper can't fly until he lose weight!")
            else:
                self.weight += changes
        except ValueError as error:
            print(error)


chip = Chip()
dale = Dale()
rocky = Rocky()
zipper = Zipper()
gadget = Gadget()

print(f'tiredness before jump -> {chip.tiredness}')
chip.jump()
print(f'tiredness after rest -> {chip.tiredness}')
print()

print(f'tiredness before fly -> {zipper.tiredness}')
zipper.fly()
print(f'tiredness after fly -> {zipper.tiredness}')
print()

print(f"Chip's weight before: {chip.weight}")
chip.change_weight()
print(f"Chip's weight after: {chip.weight}")
print()

print(f"Dale's weight before: {dale.weight}")
dale.change_weight(0.06)
print(f"Dale's weight after: {dale.weight}")
print()

zipper.change_weight(0.012)
print(f"Zipper's weight: {zipper.weight}")
