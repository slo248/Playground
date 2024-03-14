from abc import ABC, abstractmethod
from HouseBuilder import *

class Director:
    def __init__(self,builder=None):
        if builder:
            assert isinstance(builder,HouseBuilder)
        self.builder=builder

    def changeBuilder(self,builder):
        assert isinstance(builder,HouseBuilder)
        self.builder=builder

    @abstractmethod
    def make(self):
        pass

class SimpleDirector(Director):
    def __init__(self,builder):
        super().__init__(builder)

    def make(self):
        self.builder.buildWindows(4)
        self.builder.buildDoors(4)
        self.builder.buildRooms(6)
        self.builder.buildGarden(True)

class LuxuryDirector(Director):
    def __init__(self,builder):
        super().__init__(builder)

    def make(self):
        self.builder.buildWindows(6)
        self.builder.buildDoors(6)
        self.builder.buildRooms(10)
        self.builder.buildPool(True)
        self.builder.buildGarden(True)
        self.builder.buildGarage(True)
