from abc import ABC, abstractmethod


class Rescuers(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError


class Man(Rescuers):

    def run(self):
        print()
