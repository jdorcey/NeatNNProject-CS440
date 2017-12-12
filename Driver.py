import Qnet
from TOH import TOH
from TwentyFortyEight import TwentyFortyEight
import os
import psutil
import time

def main():
        
    #the memory usage before the start of the current Python process
    process = psutil.Process(os.getpid())
    startMem = process.memory_info().rss/10**9, 'GB'

    hiddenLayers = [40]
    nReplays = 0
    nIterations = 20
    epsilon = 0.8
    epsilonDecayFactor = 0.99
    nReplays = 0
    toh = TOH()
    tfe = TwentyFortyEight()
<<<<<<< HEAD
    
    #Start training TOH
    print("TOWERS OF HANOI:")
    startTohTrain = time.time()
    qnet, outcomes, samples = Qnet.trainQnet(100, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, toh)
    endTohTrain = time.time() - startTohTrain
    print("TOTAL TIME TO TRAIN TOWERS OF HANOI: ", endTohTrain)
    
    #Start testing TOH
    #startTohTest = time.time()    
    #endTohTest = time.time() - startTohTest

    #Start training TwentyFortyEight
    print()
    print("TWENTY FORTY EIGHT:")
    startTfeTrain = time.time()
    qnet, outcomes, samples = Qnet.trainQnet(100, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, tfe)
    endTfeTrain = time.time() - startTfeTrain
    print("TOTAL TIME TO TRAIN TWENTY FORTY EIGHT: ", endTfeTrain)
    
    #Start testing TFE
    #startTfeTest = time.time()
    #endTfeTest = time.time() - startTfeTest
=======
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
>>>>>>> master
   
    #the memory usage after the process completes
    endMem = process.memory_info().rss/10**9, 'GB'
    totalMem = endMem[0] - startMem[0] 
    print()
    print("TOTAL MEMORY USED BY PROGRAM IN GB: ", totalMem) 
    
<<<<<<< HEAD
=======
 
>>>>>>> 4b1a2b89abd2b9a45fcd9f4aa2aebf1e843d90af
>>>>>>> master
if __name__ == "__main__":
    main()