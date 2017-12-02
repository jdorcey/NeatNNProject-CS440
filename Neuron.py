# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:47:11 2017

@author: Tom Shaw
"""

class Neuron:
    def __init__(self):
        #input weights
        self.w = []
        #input values
        self.v = []
        self.value = 0
        self.out = []
        self.outIndex = []
    
    def shareValue(self, index, value):
        self.v[index] = value
        return
    
    def makeAFriend(self, other):
        self.out.append(other)
        self.outIndex.append(other.addWeight())
        return
    
    def addWeight(self):
        newIndex = len(self.w)
        self.w.append()
        self.v.append()
        return newIndex
    
    def calculate(self):
        sum = 0
        for i in range(len(self.w)):
            sum+=(self.w[i]*self.v[i])
        self.value = sum
        return
    
    def share(self):
        for i in range(len(self.out)):
            self.out[i].shareValue(self.outindex[i], self.sum)
        return
    
    def getValue(self):
        return self.value