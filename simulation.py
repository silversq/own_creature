from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import constants as c

class SIMULATION:
    def __init__(self, directOrGUI, solutionId):
        self.solutionId = solutionId
        self.directOrGUI = directOrGUI
        if directOrGUI == 'DIRECT':
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT(solutionId)

        p.setGravity(0,0,-90.8)
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
    def Run(self):
        
        for i in range(c.nSteps):
            p.stepSimulation()
            self.robot.SENSE(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == 'GUI':
                time.sleep(1/60)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness(self.solutionId)