from abc import ABC, abstractmethod


class Rescuers(ABC):

    @abstractmethod
    def run(self):
        pass


class Man(Rescuers):

    @abstractmethod
    def jump(self):
        pass


class Women(Man):
    def run(self):
        print('i can run')

    def jump(self):
        print('i can jump')


rescuers = Women()
rescuers.jump()
rescuers.run()
