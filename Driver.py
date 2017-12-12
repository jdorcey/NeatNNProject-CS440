# -*- coding: utf-8 -*-
#@author: Tom Shaw and Jennifer Dorcey

import Qnet
from TOH import TOH
from TwentyFortyEight import TwentyFortyEight
import os
import psutil
import time

def main():
    
    #the memory usage before the start of the current Python process
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss/10**9, 'GB')


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
<<<<<<< HEAD






=======
   
    #the memory usage after the current Python process
    print(process.memory_info().rss/10**9, 'GB')
    
 
>>>>>>> 4b1a2b89abd2b9a45fcd9f4aa2aebf1e843d90af
if __name__ == "__main__":
    main()
