from abc import ABC, abstractmethod
from vehicle import *

class Logistic(ABC):
    @abstractmethod
    def createTransport(self):
        pass

    def execute(self, pkg):
        vehicle = self.createTransport()
        vehicle.transport(pkg)

class TruckLogistic(Logistic):
    def createTransport(self):
        return Truck()
    
class ShipLogistic(Logistic):
    def createTransport(self):
        return Ship()
