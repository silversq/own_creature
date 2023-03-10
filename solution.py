import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myId = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights*10-10
    
    def Set_ID(self, iD):
        self.myId = iD
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system('start /B py simulate.py ' + directOrGUI + ' ' + str(self.myId))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myId) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myId) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness" + str(self.myId) + ".txt")

    def Mutate(self):
        randrow = random.randint(0, c.numSensorNeurons-1)
        randcol = random.randint(0, c.numMotorNeurons-1)
        self.weights[randrow, randcol] = random.random()*2-1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        pyrosim.Send_Cube(name="Box", pos=[0,-1,3] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_SDF("world.sdf")
        length = 2
        width = 1
        height = 1
        pyrosim.End()
        pyrosim.Start_URDF("cube.urdf")
        pyrosim.Send_Cube(name="Box", pos=[0,3,2] , size=[0.5,0.5,0.5], mass=0.1)
        pyrosim.End()
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height], mass=999)
        # pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0, -0.5, 1], jointAxis = "1 0 0")
        # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
        # pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.0,0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "RightLeg_RightLeg2" , parent= "RightLeg" , child = "RightLeg2" , type = "revolute", position = [0, 0.5, 0], jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "RightLeg2_RightLeg3" , parent= "RightLeg2" , child = "RightLeg3" , type = "revolute", position = [0, 0.5, 0], jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "RightLeg3_RightLeg4" , parent= "RightLeg3" , child = "RightLeg4" , type = "revolute", position = [0, 0.5, 0], jointAxis = "1 0 0")
        pyrosim.Send_Joint( name = "RightLeg4_RightLeg5" , parent= "RightLeg4" , child = "RightLeg5" , type = "revolute", position = [0, 0.5, 0], jointAxis = "1 0 0")

        pyrosim.Send_Joint( name = "RightLeg5_Platform" , parent= "RightLeg5" , child = "Platform" , type = "revolute", position = [0, 0.5, 0], jointAxis = "1 0 0")

        # pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = [0, -1, 0], jointAxis = "0 1 1")
        # pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0, 1, 0], jointAxis = "0 1 1")
        # pyrosim.Send_Joint( name = "LeftLeg_LowerLeftLeg" , parent= "LeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = [-1, 0, 0], jointAxis = "0 1 1")
        # pyrosim.Send_Joint( name = "RightLeg_LowerRightLeg" , parent= "RightLeg" , child = "LowerRightLeg" , type = "revolute", position = [1, 0, 0], jointAxis = "0 1 1")
        # pyrosim.Send_Joint( name = "LeftLeg_Platform2" , parent= "LeftLeg" , child = "Platform2" , type = "revolute", position = [0.5,-0.8,0], jointAxis = "1 0 0")

        # pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        # pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        # pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        # pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5] , size=[0.2,0.2,1])

        # pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.1,-0.5,0] , size=[0.2,2,0.2])
        # pyrosim.Send_Cube(name="LeftLeg2", pos=[-0.1,-0.5,0] , size=[0.2,2,0.2])

        pyrosim.Send_Cube(name="RightLeg", pos=[0.0,0.25,0] , size=[0.2,0.5,0.2], mass=0.1)
        pyrosim.Send_Cube(name="RightLeg2", pos=[0.0,0.25,0] , size=[0.2,0.5,0.2], mass=0.1)
        pyrosim.Send_Cube(name="RightLeg3", pos=[0.0,0.25,0] , size=[0.2,0.5,0.2], mass=0.1)
        pyrosim.Send_Cube(name="RightLeg4", pos=[0.0,0.25,0] , size=[0.2,0.5,0.2], mass=0.1)
        pyrosim.Send_Cube(name="RightLeg5", pos=[0.0,0.25,0] , size=[0.2,0.5,0.2], mass=0.1)

        pyrosim.Send_Cube(name="Platform", pos=[0,0.5,0] , size=[1, 1, 0.1], mass=0.1)
        # pyrosim.Send_Cube(name="Platform2", pos=[0,0,0] , size=[1, 1, 0.1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myId) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Platform")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "Platform2")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LowerFrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LowerRightLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LowerLeftLeg")

        # pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 2 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 1 , jointName = "RightLeg_RightLeg2")
        pyrosim.Send_Motor_Neuron( name = 2 , jointName = "RightLeg5_Platform")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "RightLeg2_RightLeg3")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "RightLeg3_RightLeg4")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "RightLeg4_RightLeg5")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_RightLeg")

        # pyrosim.Send_Motor_Neuron( name = 8 , jointName = "RightLeg_LowerRightLeg")
        # pyrosim.Send_Motor_Neuron( name = 9 , jointName = "LeftLeg_LowerLeftLeg")
        # pyrosim.Send_Motor_Neuron( name = 10 , jointName = "BackLeg_LowerBackLeg")
        # pyrosim.Send_Motor_Neuron( name = 11 , jointName = "FrontLeg_LowerFrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+1, weight = self.weights[currentRow][currentColumn])

        pyrosim.End()