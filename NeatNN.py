# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:27:23 2017

@author: Tom Shaw
"""
import Neuron
import random as r
import Neat


class NeatNeuralNetwork:

    def __init__(self, problem):
        self.problem = problem
        self.network = [[len(problem.input)], [len(problem.allMoves)]]

    # calculates the value of each neuron and passes it to the next layer
    # returns the value of the last layer of neurons
    def calculate(self):
        self.zeroLayer()
        values = []
        for i in range(len(self.network)):
            for j in range(len(self.network[i])):
                self.network[i][j].compute()
                self.network[i][j].share()
        for j in range(len(self.network[-1])):
            values.append(self.network[-1][j].getValue())
        return values

    # should go through and input the intial values
    # into the first layer of the NN
    def zeroLayer(self):
        for i in range(len(problem.input)):
            self.network[0][i].value[0] = problem.input[i]
        return

    # changes a weight to include a neuron in the middle
    # neuron-neuron -> neuron-neuron-neuro
    # with a random weight to the third neuron
    def addNeuron(self):
        # get the name for the new neuron
        global Name
        weights = self.getWeights()
        # get information about the gene that we are adding a neuron to
        toNeuron, index, fromNeuron = r.choice(weights)
        x1, y1 = toNeuron.getNNetIndex()
        x2, y2 = fromNeuron.getNNetIndex()
        # compute elements of new neuron
        x3 = ((x1 + x2) / 2)
        if x3 == x1:
            y3 = 0
        else:
            y3 = len(self.network[x3])
        new = Neuron(Name, x3, y3)
        Name += 1
        # add in neuron to the right place
        if x3 == x1:
            self.network.insert(x1+1, new)
        elif x3 == x2:
            self.network.insert(x2-1, new)
        else:
            self.network.insert(x3, new)
        # add in new weights
        new.makeAFriend(toNeuron, index)
        fromNeuron.makeAFriend(new)
        fromNeuron.removeNeuron(toNeuron)
        return

    # adds a gene to a random neuron-neuron combination
    def addWeight(self):
        # get the from neuron
        neurons = []
        for i in range(len(self.network)-1):
            for j in range(len(self.network[i])):
                neurons.append[self.network[i][j]]
        # TODO here
        return

    # method that changes the value of 2-3 weights
    def changeWeights(self):
        rand = r.randint(2, 3)
        for i in range(rand):
            self.changeWeight
        return

    # determines of a mutation should occur and if so,
    # which mutation should happen
    def mutate(self):
        rand = r.uniform(0, 10)
        if rand < 2:
            self.addNeuron()
        elif rand < 5:
            self.addWeight()
        self.changeWeights()
        return

    # changes the weight of a random gene
    # determines a high or low read and changes the weight to be either:
    # low: change weight to midpoint of -1-weight
    # high: change weight to be midpoint of weight-1
    def changeWeight(self):
        weights = self.getWeights()
        toNeuron, index, fromNeuron = r.choice(weights)
        rand = r.randint(0, 10)
        if rand < 5:
            toggle = False
            toNeuron.cWeight(index, toggle)
        else:
            toggle = True
            toNeuron.cWeight(index, toggle)
        return

    # gets a neuron, index combo for every out
    # going node skipping the last layer
    def getWeights(self):
        ret = []
        for layer in self.network:
            for node in layer:
                for w in node.getWeights:
                    ret.append(w)
        return ret

    # returns the value of the fitness as described by the problem
    def fitness(self):
        return self.problem.fitness()
