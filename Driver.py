# -*- coding: utf-8 -*-
#@author: Tom Shaw and Jennifer Dorcey

import Qnet
from TOH import TOH
from TwentyFortyEight import TwentyFortyEight
import time
import random

def main():
   
    
    hiddenLayers = [40]
    nReplays = 0
    nIterations = 10
    epsilon = 0.5
    epsilonDecayFactor = 0.99
    nReplays = 0
    #toh = TOH(6)
    tfe = TwentyFortyEight()
    
    
    #time training
    startTrainTime = time.time()
    print("START TRAIN: ", startTrainTime)
    qnet, outcomes, samples = Qnet.trainQnet(300, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, tfe)
    endTrainTime = time.time() - startTrainTime
    print("EBD TRAIN: ", endTrainTime)
    
    #time testing
    #startTestTime = time.time()
    
    
    #endTestTime = time.time() - startTestTime
    '''
    

    tfe = TwentyFortyEight()
   
    
    tfe.randomTile()
    print(tfe)
    
    while tfe.validMoves():
        print(tfe.validMoves())
        k = random.choice(tfe.validMoves())
        print(k)
        tfe.makeMove(k)
        print("MAKE MOVE")
        print(tfe)
     
    print(tfe) 
    '''
   
if __name__ == "__main__":
    main()
