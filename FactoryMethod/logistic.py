from abc import ABC, abstractmethod
from vehicle import *

class Logistic(ABC):
    @abstractmethod
    def createTransport(self):
        pass

    def execute(self):
        vehicle = self.createTransport()
        vehicle.transport()

class TruckLogistic(Logistic):
    def createTransport(self):
        return Truck()
    
class ShipLogistic(Logistic):
    def createTransport(self):
        return Ship()
