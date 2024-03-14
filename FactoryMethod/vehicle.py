from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def transport(self,pkg):
        pass

class Truck(Vehicle):
    def transport(self,pkg):
        print(f'Truck is transporting {pkg}')

class Ship(Vehicle):
    def transport(self,pkg):
        print(f'Ship is transporting {pkg}')
