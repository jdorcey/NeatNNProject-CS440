# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:32:10 2017

@author: Tom Shaw
"""
import Qnet
from TOH import TOH

def main():
    
    toh = TOH(4)
    print(toh)
    
    currState = [[], [1], [2, 3, 4]]
    print(toh.goalTest(currState))
    
    '''
    hiddenLayers = [40]
    nReplays = 0
    nIterations = 10
    epsilon = 0.5
    epsilonDecayFactor = 0.99
    nReplays = 0
    toh = TOH()
    qnet, outcomes, samples = Qnet.trainQnet(300, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, toh.validMoves, toh.makeMove)
    '''
    
if __name__ == "__main__":
    main()
