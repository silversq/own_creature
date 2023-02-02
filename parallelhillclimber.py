import constants as c
from solution import SOLUTION
import copy
import os
class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def EVOLVE(self):
        self.Evaluate(self.parents)
            # print("\nFITNESS: " + str(self.parents[parent].fitness))
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        

    def Show_Best(self):
        lowest_parent = self.parents[0]
        for i in self.parents.keys():
            if self.parents[i].fitness < lowest_parent.fitness:
                lowest_parent = self.parents[i]
        print('\n Lowest fitness: ' + str(lowest_parent.fitness) + '\n')
        lowest_parent.Start_Simulation('GUI')

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        print('\n')        
        self.Print()
        print('\n')
        self.Select()

    def Spawn(self):
        self.children = {}
        for parent in self.parents.keys():
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.nextAvailableID += 1
            self.children[parent].Set_ID(self.nextAvailableID)

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation('DIRECT')
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()
        
    def Print(self):
        for i in self.parents.keys():
            print("\nParent: " + str(self.parents[i].fitness) + " Child: " + str(self.children[i].fitness))

    def Select(self):
        for i in self.parents.keys():
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]
