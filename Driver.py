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
    toh = TOH(6)
    #tfe = TwentyFortyEight()
    '''
    
    #time training
    startTrainTime = time.time()
    print(startTrainTime)
    
    qnet, outcomes, samples = Qnet.trainQnet(300, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, toh)
    endTrainTime = time.time() - startTrainTime
    print(endTrainTime)
    
    #time testing
    #startTestTime = time.time()
    
    
    #endTestTime = time.time() - startTestTime
    
    
    '''
    tfe = TwentyFortyEight()
    
    
    tfe.randomTile()
    print(tfe)
    for i in range(50):
        moves = tfe.ValidMoves()
        print(moves)
        move = random.choice(moves)
        print(move)
        tfe.makeMove(move)
    
        print(tfe)
        
if __name__ == "__main__":
    main()
