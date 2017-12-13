import Qnet
from TOH import TOH
from TwentyFortyEight import TwentyFortyEight
import os
import psutil
import time
from Neat import Neat

def main():
        
    #the memory usage before the start of the current Python process
    #process = psutil.Process(os.getpid())
    #startMem = process.memory_info().rss/10**9, 'GB'

    hiddenLayers = [40]
    nReplays = 0
    nIterations = 20
    epsilon = 0.8
    epsilonDecayFactor = 0.99
    nReplays = 0
    toh = TOH()
    tfe = TwentyFortyEight()
    
<<<<<<< HEAD
    net = Neat(tfe)
=======
<<<<<<< HEAD
    
    #Start training TOH
    print("TOWERS OF HANOI:")
    startTohTrain = time.time()
    qnet, outcomes, samples = Qnet.trainQnet(50, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, toh)
    endTohTrain = time.time() - startTohTrain
    print("TOTAL TIME TO TRAIN TOWERS OF HANOI: ", endTohTrain)
=======
    net = Neat(toh)
>>>>>>> 2b40a402dc4fa328ca27ca993656185a217e3ea7
    net.train()
    
    
    
    #Start training TOH
    #print("TOWERS OF HANOI:")
    #startTohTrain = time.time()
    #qnet, outcomes, samples = Qnet.trainQnet(100, hiddenLayers, nIterations, nReplays, epsilon, epsilonDecayFactor, toh)
    #endTohTrain = time.time() - startTohTrain
    #print("TOTAL TIME TO TRAIN TOWERS OF HANOI: ", endTohTrain)
>>>>>>> 0294d32b34b2aeba41d474dfc6ce5d94d2550af3
    
    #Start testing TOH
    #startTohTest = time.time()    
    #endTohTest = time.time() - startTohTest

    #Start training TwentyFortyEight
<<<<<<< HEAD
    print()
    print("TWENTY FORTY EIGHT:")
    startTfeTrain = time.time()
    qnet, outcomes, samples = Qnet.trainQnet(50, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, tfe)
    endTfeTrain = time.time() - startTfeTrain
    print("TOTAL TIME TO TRAIN TWENTY FORTY EIGHT: ", endTfeTrain)
=======
    #print()
    #print("TWENTY FORTY EIGHT:")
    #startTfeTrain = time.time()
    #qnet, outcomes, samples = Qnet.trainQnet(100, hiddenLayers, nIterations, nReplays, epsilon, epsilonDecayFactor, tfe)
    #endTfeTrain = time.time() - startTfeTrain
    #print("TOTAL TIME TO TRAIN TWENTY FORTY EIGHT: ", endTfeTrain)
>>>>>>> 0294d32b34b2aeba41d474dfc6ce5d94d2550af3
    
    #Start testing TFE
    #startTfeTest = time.time()
    #endTfeTest = time.time() - startTfeTest
   
    #the memory usage after the process completes
    #endMem = process.memory_info().rss/10**9, 'GB'
    #totalMem = endMem[0] - startMem[0] 
    #print()
    #print("TOTAL MEMORY USED BY PROGRAM IN GB: ", totalMem) 
    
if __name__ == "__main__":
    main()