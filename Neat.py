# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:33:44 2017

@author: Tom Shaw and Jenn Dorcey
"""


class Neat:
    def __init__(self, problem):
        # TODO write constructor
        global Name = 0
        self.problem = problem
        self.networks = []
        self.results = []
        pass

    # this method is the hub for training a neural network from scratch
    def train(self):
        # generate a new population of networks
        self.generateInitalPopulation()
        # train until a champion hits optimal fitness
        while self.chooseChampion.fitness != problem.getOptimal():
            # print out the results of the last iteration
            if self.results:
                print(results[-1])
            self.runNetworks()
            self.breedNetworks()
            # TODO add to results somehow
        return results

    # This method is for testing the current champion
    def test(self):
        # TODO add this in
        pass

    # This method runs all the currently generated networks
    # TODO make this concurrent
    def runNetworks(self):
        # TODO write this in
        pass

    # this method is resposible for breeding all the current networks
    def breedNetworks(self):
        newNetworks = []
        self.prunePopulation()
        # breed all standing networks with the champion
        # may produce more than 100 networks but will be in the neighborhood
        while len(self.networks) < 100:
            for i in range(1, len(self.networks)):
                self.breedTwo(0, i)
        # mutate all current networks 3 times
        self.mutateNetworks(3)
        return

    # this method removes the lower half of the networks
    # this method also removes any network with a fitness of 0
    def prunePopulation(self):
        # remove all networks with a 0 fitness
        for net in self.networks:
            if net.fitness() == 0:
                self.networks.remove(net)
        self.sortNetworks()
        if len(self.networks) > 50:
            for i in range(50, len(self.networks)):
                self.networks.remove(i)
        return

    # this method sorts networks based on their fitness
    # highest fitnesses have the lower indexes
    def sortNetworks(self):
        # TODO write this in
        pass

    # this method is for breeding two individual networks
    def breedTwo(self, indexOne, indexTwo):
        # TODO write this in
        pass

    # this method is for signaling networks to mutate
    # ignores the champion
    def mutateNetworks(self, iterations):
        # TODO write this in
        pass

    # generates an inital set of networks
    # these networks are starting from scratch
    # so they need to be highly mutated at the start
    def generateInitalPopulation(self):
        # TODO write this in
        pass

    # This method selects the most successful
    # network from the current generation
    def chooseChampion(self):
        # TODO add this in
        pass
