from abc import ABC, abstractmethod

class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

class VictorianChair(Chair):
    def sit(self):
        print('You are sitting on a Victorian chair.')

class ModernChair(Chair):
    def sit(self):
        print('You are sitting on a modern chair.')

class WoodChair(Chair):
    def sit(self):
        print('You are sitting on a wood chair.')


