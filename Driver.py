# -*- coding: utf-8 -*-
#@author: Tom Shaw and Jennifer Dorcey

import Qnet
from TOH import TOH
from TwentyFortyEight import TwentyFortyEight
import time

def main():

    hiddenLayers = [40]
    nReplays = 0
    nIterations = 2
    epsilon = 0.8
    epsilonDecayFactor = 0.99
    nReplays = 0
    toh = TOH()
    tfe = TwentyFortyEight()
    tfe.randomTile()
    
    
    
    #time training
    startTrainTime = time.time()
    print("START TRAIN: ", startTrainTime)
    qnet, outcomes, samples = Qnet.trainQnet(5, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, tfe)
    endTrainTime = time.time() - startTrainTime
    print("END TRAIN: ", endTrainTime)
    
    #time testing
    #startTestTime = time.time()
    
    
    #endTestTime = time.time() - startTestTime
    
    

    
    
 
if __name__ == "__main__":
    main()
