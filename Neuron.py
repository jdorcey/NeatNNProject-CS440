# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:47:11 2017

@author: Tom Shaw
"""


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

    def shareValue(self, index):
        self.v[index] = self.value
        return

    def makeAFriend(self, other):
        self.out.append(other)
        self.outIndex.append(other.addWeight())
        return

    def makeAFriend(self, other, index):
        self.out.append(other)
        self.outIndex.append(index)
        return

    def addWeight(self):
        newIndex = len(self.w)
        self.w.append()
        self.v.append()
        return newIndex

    def calculate(self):
        sum = 0
        for i in range(len(self.w)):
            sum += (self.w[i]*self.v[i])
        self.value = sum
        return

    def share(self):
        for i in range(len(self.out)):
            self.out[i].shareValue(self.outindex[i])
        return

    def getValue(self):
        return self.value

    def getWeights(self):
        return [(self.out[i], self.outIndex[i], self)
                for i in range(len(self.out))]

    def cWeight(self, index, toggle):
        self.weight = w[index]
        if toggle:
            weight = ((weight + 1)/2)
        else:
            weight = ((weight - 1)/2)
        self.w[index] = weight
        return

    def getNNetIndex(self):
        return (self.nnlayer, self.nnlindex)

    def removeNeuron(self, other):
        for i in range(len(self.out)):
            if out[i].name == other.name:
                self.out.remove(i)
                self.outIndex.remove(i)
        return
