# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:27:23 2017

@author: Tom Shaw
"""
import Neuron
import random as r

class NeatNeuralNetwork:
    def __init__(self, problem):
        self.problem = problem
        self.network = [[len(problem.input)],[len(problem.allMoves)]]
        
    #calculates the value of each neuron and passes it to the next layer
    #returns the value of the last layer of neurons
    def calculate(self):
        #TODO add in 0th layer calculations 
        values = []
        for i in range(len(self.network)):
            for j in range(len(self.network[i])):
                self.network[i][j].compute()
                self.network[i][j].share()
        for j in range(len(self.network[-1])):
            values.append(self.network[-1][j].getValue())
        return values
    
    #changes a weight to include a neuron in the middle
    #with a random weight to the third neuron
    def addNeuron(self):
        pass
    
    #adds a weight to a random neuron-neuron combination
    def addWeight(self):
        pass
    
    #determines of a mutation should occur and if so, which mutation should happen
    def mutate(self):
        pass
    
    #changes the weight of a random gene
    #determines a high or low read and changes the weight to be either:
    #low: change weight to midpoint of 0-weight
    #high: change weight to be midpoint of weight-1
    def changeWeight(self):
        pass
    
    #returns the value of the fitness as described by the problem
    def fitness(self):
        return self.problem.fitness()
    