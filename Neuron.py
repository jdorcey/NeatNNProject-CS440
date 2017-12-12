# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:47:11 2017

@author: Tom Shaw
"""
import random as r


class Neuron:
    def __init__(self, thisname, x, y):
        self.inNeurons = []
        # input weights
        self.w = []
        # input values
        self.v = []
        self.value = 0
        # output neurons
        self.out = []
        self.outIndex = []
        self.name = thisname
        self.nnlayer = x
        self.nnlindex = y

    # pass value to another neuron
    def shareValue(self, index):
        self.v[index] = self.value
        return

    # add a weight between this neuron and another neuron
    def makeAFriend(self, other):
        self.out.append(other)
        self.outIndex.append(other.addWeight())
        return

    # add a weight with this neuron and another
    # used when a neuron takes the place of another
    def makeAFriend(self, other, index):
        self.out.append(other)
        self.outIndex.append(index)
        return

    # adds capacity for a neuron and its associated value
    # adds a random weight as an initial value
    # returns the index to where fromNeuron should store value
    def addWeight(self):
        newIndex = len(self.w)
        self.w.append(r.uniform(-1, 1))
        self.v.append()
        return newIndex

    # sums the input values and their weights
    def calculate(self):
        sum = 0
        for i in range(len(self.w)):
            sum += (self.w[i]*self.v[i])
        self.value = sum
        return

    # method that controls sharing to all output neurons
    def share(self):
        for i in range(len(self.out)):
            self.out[i].shareValue(self.outindex[i])
        return

    # a getter for the current value
    def getValue(self):
        return self.value

    # returns a list of all the weights this neuron is responsible for
    def getWeights(self):
        return [(self.out[i], self.outIndex[i], self)
                for i in range(len(self.out))]

    # a method that changes a random weight
    def cWeight(self, index, toggle):
        self.weight = w[index]
        if toggle:
            weight = ((weight + 1)/2)
        else:
            weight = ((weight - 1)/2)
        self.w[index] = weight
        return

    # returns thsi neuron's indexing for the neural network its in
    def getNNetIndex(self):
        return (self.nnlayer, self.nnlindex)

    # given another neuron, finds and removes the neruon from the outlist
    def removeNeuron(self, other):
        for i in range(len(self.out)):
            if out[i].name == other.name:
                self.out.remove(i)
                self.outIndex.remove(i)
        return
