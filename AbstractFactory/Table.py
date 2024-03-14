from abc import ABC, abstractmethod

class Table(ABC):
    @abstractmethod
    def doSth(self):
        pass

class VictorianTable(Table):
    def doSth(self):
        print('You are using a Victorian table.')

class ModernTable(Table):
    def doSth(self):
        print('You are using a modern table.')

class WoodTable(Table):
    def doSth(self):
        print('You are using a wood table.')


