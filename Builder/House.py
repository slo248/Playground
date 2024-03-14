class House:
    def __init__(self):
        self.windows=self.doors=self.rooms=0
        self.hasPool=self.hasGarden=self.hasGarage=False
    
    def setWindows(self,amount):
        assert isinstance(amount,int) and amount>=0
        self.windows=amount

    def setDoors(self,amount):
        assert isinstance(amount,int) and amount>=0
        self.doors=amount

    def setRooms(self,amount):
        assert isinstance(amount,int) and amount>=0
        self.rooms=amount

    def setPool(self,flag):
        assert isinstance(flag,bool)
        self.hasPool=flag
    
    def setGarden(self,flag):
        assert isinstance(flag,bool)
        self.hasGarden=flag

    def setGarage(self,flag):
        assert isinstance(flag,bool)
        self.hasGarage=flag

    def __str__(self):
        return (f'This house have following properties:\n'
                f'Windows: {self.windows}\n'
                f'Doors: {self.doors}\n'
                f'Rooms: {self.rooms}\n'
                f'Swimming pool: {self.hasPool}\n'
                f'Garden: {self.hasGarden}\n'
                f'Garage: {self.hasGarage}')
