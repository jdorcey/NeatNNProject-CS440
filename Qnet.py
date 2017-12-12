import numpy as np
import random
import matplotlib.pyplot as plt
import neuralnetworks as nn
from copy import deepcopy

def epsilonGreedy(Qnet, epsilon, game):
    moves = game.validMoves()
    if np.random.uniform() < epsilon: # random move
        move = moves[random.sample(range(len(moves)),1)[0]]
        Q = Qnet.use(np.array([game.newStateRep() + move])) if Qnet.Xmeans is not None else 0
    else:                           # greedy move
        qs = []
        for m in moves:
            qs.append(Qnet.use(np.array([game.newStateRep() + m])) if Qnet.Xmeans is not None else 0)
        move = moves[np.argmax(qs)]
        Q = np.max(qs)
    return move, Q
	
def trainQnet(nReps, hiddenLayers, nIterations, nReplays, epsilon, epsilonDecayFactor, game):
    outcomes = np.zeros(nReps)
    
    
    n = game.inputSize()
    Qnet = nn.NeuralNetwork(n, hiddenLayers, 1)
    Qnet._standardizeT = lambda x: x
    Qnet._unstandardizeT = lambda x: x

    samples = []  # collect all samples for this repetition, then update the Q network at end of repetition.
    for rep in range(nReps):
        if rep > 0:
            epsilon *= epsilonDecayFactor
        step = 0
        done = False

        samples = []
        samplesNextStateForReplay = []
        
        move, _ = epsilonGreedy(Qnet, epsilon, game)
        while not done:
            step += 1
            
           # Make this move to update toh.state
            game.makeMove(move)
            r = -1
            
            # Choose move from updated toh.state
            moveNext, Qnext = epsilonGreedy(Qnet, epsilon, game)
 
            if game.gameOver():
                # goal found
                Qnext = 0
                done = True
                outcomes[rep] = step
                
                if rep % 10 == 0 or rep == nReps - 1:
                    print('rep= {:d} epsilon= {:.3f} steps= {:d}'.format(rep, epsilon, int(outcomes[rep])), end='\n')
               
            samples.append([*game.newStateRep(), *move, r, Qnext])
            samplesNextStateForReplay.append([*game.newStateRep(), *moveNext])
            
            move = deepcopy(moveNext)
            
        samples = np.array(samples)
        X = samples[:,:n]
        T = samples[:,n:n+1] + samples[:,n+1:n+2]
        Qnet.train(X, T, nIterations, verbose=False)

        # Experience Replay: Train on recent samples with updates to Qnext.
        samplesNextStateForReplay = np.array(samplesNextStateForReplay)
        for replay in range(nReplays):
            QnextNotZero = samples[:,n+1] != 0
            samples[QnextNotZero, n+1:n+2] = Qnet.use(samplesNextStateForReplay[QnextNotZero,:])
            T = samples[:,n+1:n+2] + samples[:,n+1:n+2]
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
	

