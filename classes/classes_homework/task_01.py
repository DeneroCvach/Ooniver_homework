from datetime import datetime


class Human:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.human_sleeping = False

    @staticmethod
    def say_hello(stranger):
        print(f"Hello {stranger}, i'm human!")

    def sleep(self):
        today = datetime.now()
        if not self.human_sleeping:
            if 9 < today.hour < 24:
                self.human_sleeping = True
                print(f'{self.name} is beasy, learning Python!')
            else:
                print(f'{self.name} sleeping right now..')

    def wake_up(self):
        if self.human_sleeping:
            self.human_sleeping = False
            print(f'{self.name} already awake and learning python!')
        else:
            print(f'{self.name} is trying to wake up! Wait a second..')


person = Human('Ivan', 190, 80)
person.say_hello('Maria')
person.sleep()
person.wake_up()
