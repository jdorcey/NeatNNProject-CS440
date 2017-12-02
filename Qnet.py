import numpy as np
import random
import matplotlib.pyplot as plt
import neuralnetworks as nn
from copy import deepcopy

def epsilonGreedy(Qnet, epsilon, toh):
    moves = toh.validMoves()
    if np.random.uniform() < epsilon: # random move
        move = moves[random.sample(range(len(moves)),1)[0]]
        Q = Qnet.use(np.array([toh.newStateRep() + move])) if Qnet.Xmeans is not None else 0
    else:                           # greedy move
        qs = []
        for m in moves:
            qs.append(Qnet.use(np.array([toh.newStateRep() + m])) if Qnet.Xmeans is not None else 0)
        move = moves[np.argmax(qs)]
        Q = np.max(qs)
    return move, Q
	
def trainQnet(nReps, hiddenLayers, nIterations, nReplays, epsilon, epsilonDecayFactor, toh):
    outcomes = np.zeros(nReps)
    Qnet = nn.NeuralNetwork(5, hiddenLayers, 1)
    Qnet._standardizeT = lambda x: x
    Qnet._unstandardizeT = lambda x: x
    # epsilon = 1.0

    samples = []  # collect all samples for this repetition, then update the Q network at end of repetition.
    for rep in range(nReps):
        if rep > 0:
            epsilon *= epsilonDecayFactor
        step = 0
        done = False

        samples = []
        samplesNextStateForReplay = []
        
        state = [[1,2,3],[],[]]
        move, _ = epsilonGreedy(Qnet, epsilon, toh)
 
        while not done:
            step += 1
            
           # Make this move to get to nextState
            stateNext = toh.makeMove(move)
            r = -1
            # Choose move from nextState
            moveNext, Qnext = epsilonGreedy(Qnet, epsilon, toh)
 
            if len(stateNext[2]) == 3:
                # goal found
                Qnext = 0
                done = True
                outcomes[rep] = step
                if rep%10 == 0 or rep == nReps-1:
                    print('rep={:d} epsilon={:.3f} steps={:d}'.format(rep, epsilon, int(outcomes[rep])), end=', ')
               
            samples.append([*toh.newStateRep(), *move, r, Qnext])
            samplesNextStateForReplay.append([*toh.newStateRep(), *moveNext])

            state = deepcopy(stateNext)
            move = deepcopy(moveNext)
            
        samples = np.array(samples)
        X = samples[:,:5]
        T = samples[:,5:6] + samples[:,6:7]
        Qnet.train(X, T, nIterations, verbose=False)

        # Experience Replay: Train on recent samples with updates to Qnext.
        samplesNextStateForReplay = np.array(samplesNextStateForReplay)
        for replay in range(nReplays):
            # for sample, stateNext in zip(samples, samplesNextStateForReplay):
                # moveNext, Qnext = epsilonGreedy(Qnet, stateNext, epsilon, validMovesF)
                # sample[6] = Qnext
            # print('before',samples[:5,6])
            QnextNotZero = samples[:,6] != 0
            samples[QnextNotZero, 6:7] = Qnet.use(samplesNextStateForReplay[QnextNotZero,:])
            # print('after',samples[:5,6])
            T = samples[:,5:6] + samples[:,6:7]
            Qnet.train(X, T, nIterations, verbose=False)

    print('DONE')
    return Qnet, outcomes, samples
	
def plotSteps(outcomes, avgOf=1):
    outcomes = outcomes.reshape((-1,avgOf)).mean(1)
    plt.plot(outcomes,'o-', label='RL Agent')
    plt.plot([0, len(outcomes)], [7, 7], 'r--', label='Shortest')
    plt.xlabel('Bins of {} repetitions'.format(avgOf))
    plt.ylabel('Steps to Reach Goal')
    plt.legend();
	

