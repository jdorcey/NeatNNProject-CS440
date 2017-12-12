# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:33:44 2017

@author: Tom Shaw and Jenn Dorcey
"""
import copy
import time


class Neat:
    def __init__(self, problem):
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
            startTime = time.time()
            self.runNetworks()
            endTime = time.time()
            self.breedNetworks()
            print("{}{}".format(self.networks[0].fitness, endTime - startTime))
            results.append([self.networks[0].fitness, endTime - startTime])
        return results

    # This method is for testing the current champion
    def test(self):
        startTime = time.time()
        champion = self.chooseChampion()
        moves = champion.runNetwork(copy.deepcopy(problem))
        endTime = time.time()
        return [moves, champion.fitness(), endTime - startTime]

    # This method runs all the currently generated networks
    # TODO make this concurrent
    def runNetworks(self):
        for net in self.networks:
            net.runNetwork(copy.deepcopy(problem))
        return

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
        tupleNets = [(net.fitness) for net in self.networks]
        tupleNets.sort(key=lambda x: x[0], reverse=True)
        # REVIEW might need to be net[1] for net in tupleNets
        self.networks = [net for fit, net in tupleNets]
        pass

    # this method is for breeding two individual networks\
    # has a .6 chance for keeping a neuron if that neuron isnt already kept
    # attempts to keep all weights associated with that neuron
    def breedTwo(self, indexOne, indexTwo):
        newNetwork = NeatNeuralNetwork(copy.deepcopy(self.problem))
        # get neurons
        newNeurons = []
        newNeurons = self.getNeurons(self.networks[indexOne], newNeurons)
        newNeurons = newNeurons + self.getNeurons(self.networks[indexTwo], newNeurons)
        # add neurons to network
        for neuron in newNeurons:
            newNetwork.addNeuron(neuron)
        # Make sure connections are valid
        newNetwork.checkConnections()
        self.networks.append(newNetwork)
        return

    # helper method that adds neurons to a list with a .6 chance
    # ignores the first and last layers as they are special cases
    def getNeurons(self, net, new):
        for i in range(1, len(net.network) - 1):
            for j in range(len(net.network)):
                if self.neruonInList(net.network[i][j], newNeurons):
                    if r.uniform(0, 1) < .6:
                        newNeurons.append(net.network[i][j])
        return newNeurons

    # a helper function that checks if a neuron is in a list
    # checks based off of neurons name
    def neruonInList(self, neuron, listOfNeurons):
        for neurons in listOfNeurons:
            if neuron.name == neurons.name:
                return True
        return False

    # this method is for signaling networks to mutate
    # ignores the champion
    def mutateNetworks(self, iterations):
        for j in range(1, len(self.networks)):
            for i in range(iterations):
                self.networks[j].mutate()
        return

    # generates an inital set of networks
    # these networks are starting from scratch
    # so they need to be highly mutated at the start
    def generateInitalPopulation(self):
        for i in range(100):
            newNetwork = NeatNeuralNetwork(copy.deepcopy(problem))
            self.networks.append(newNetwork)
        self.mutateNetworks(10)
        return

    # This method selects the highest fitness
    # network from the current generation
    def chooseChampion(self):
        self.sortNetworks()
        return self.networks[0]
