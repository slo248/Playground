from House import *

class HouseBuilder:
    def __init__(self):
        self.result=House()

    def reset(self):
        self.result=House()

    def buildWindows(self,amount):
        self.result.setWindows(amount)

    def buildDoors(self,amount):
        self.result.setDoors(amount)

    def buildRooms(self,amount):
        self.result.setRooms(amount)

    def buildPool(self,flag):
        self.result.setPool(flag)

    def buildGarden(self,flag):
        self.result.setGarden(flag)

    def buildGarage(self,flag):
        self.result.setGarage(flag)

    def getResult(self):
        return self.result
