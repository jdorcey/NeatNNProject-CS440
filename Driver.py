# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:32:10 2017

@author: Tom Shaw
"""
import Qnet
from TOH import TOH

def main():
   
    hiddenLayers = [40]
    nReplays = 0
    nIterations = 10
    epsilon = 0.5
    epsilonDecayFactor = 0.99
    nReplays = 0
    toh = TOH(3) 
    qnet, outcomes, samples = Qnet.trainQnet(300, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, toh)
    
 
if __name__ == "__main__":
    main()
