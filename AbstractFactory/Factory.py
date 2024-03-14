from abc import ABC, abstractmethod
from Chair import *
from Table import *

class Factory(ABC):
    @abstractmethod
    def createChair(self):
        pass

    @abstractmethod
    def createTable(self):
        pass

class VictorianFactory(Factory):
    def __init__(self):
        print('Victorian factory is created!')

    def createChair(self):
        return VictorianChair()
    
    def createTable(self):
        return VictorianTable()

class WoodFactory(Factory):
    def __init__(self):
        print('Wood Factory is created!')

    def createChair(self):
        return WoodChair()
    
    def createTable(self):
        return WoodTable()
