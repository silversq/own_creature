import numpy
import pyrosim.pyrosim as pyrosim
class SENSOR:
    def __init__(self, name):
        self.linkName = name
        self.values =  numpy.zeros(1000)

    def Get_Value(self, val):
        touch = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        self.values[val] = touch

    def Save_Values(self):
        numpy.save('data/SensorValues.npy', self.values)
