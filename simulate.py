import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()    
simulation.Get_Fitness()


#backLegSensorValues = numpy.zeros(1000)
#frontLegSensorValues = numpy.zeros(1000)
#frontTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*c.frontFrequency)+c.frontPhaseOffset)*(c.frontAmplitude)
#backTargetAngles = numpy.sin((numpy.linspace(0, 2*numpy.pi, 1000)*c.backFrequency)+c.backPhaseOffset)*(c.backAmplitude)


#numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
#numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
#p.disconnect()