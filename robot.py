from motor import MOTOR
from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
class ROBOT:
    def __init__(self, solutionId):
        self.nn = NEURAL_NETWORK("brain" + str(solutionId) + ".nndf")
        self.robotId = p.loadURDF("body.urdf")
        os.system('del brain' + str(solutionId) + '.nndf')
    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def SENSE(self, t):
        for i in self.sensors.values():
            i.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                jointName = bytes(jointName, 'utf-8')
                self.motors[jointName].Set_Value(self.robotId, desiredAngle*c.motorJointAngle)

    def Get_Fitness(self, solutionId):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(solutionId) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("rename tmp" + str(solutionId) + ".txt " + "fitness" + str(solutionId) + ".txt")
    def Think(self):
        self.nn.Update()
        # self.nn.Print()


        