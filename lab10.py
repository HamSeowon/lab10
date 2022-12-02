class Automobile():
    def __init__(self,ndoors=0,clr=""):
        self._doors = ndoors
        self._colour = clr

    def printDoors(self):
        return "Number of doors is:"+str(self._doors)#1

    def printColour(self,clr):
        return "Color is:" + self._colour

    def disply(self):
        return "Car is:" +str(self._doors)+" doors,"+self._colour


class SportCar(Automobile):
    def __init__(self,engine):#2
        super().__init__(ndoors,clr)
        self._engine = engine

    def disply(self):
        return "Car is"+str(self._doors)+" doors," + self._colour+", with "+str(self._engine)+" hp"
