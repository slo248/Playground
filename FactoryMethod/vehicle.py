from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def transport(pkg):
        pass

class Truck(Vehicle):
    def transport(pkg):
        print('Truck is transporting packages')

class Ship(Vehicle):
    def transport(pkg):
        print('Ship is transporting packages')
