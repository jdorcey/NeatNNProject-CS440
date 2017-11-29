import numpy as np
import random
import matplotlib.pyplot as plt
from copy import deepcopy
import neuralnetworks as nn

def printState(s):
    lens = [len(p) for p in s]
    for height in range(max(lens),0,-1):
        row = ""
        for p in range(3):
            if lens[p] >= height:
                row += str(s[p][lens[p]-height]) + ' '
            else:
                row += '  '
        print(row)
    print('------')
    print()
    
def validMoves(state):
    """Given state like [[1,2,3],[],[]]
    return valid moves, like [(1,2),(1,3)]) pairs of source and dest peg"""
    moves = []
    disksOn1,disksOn2,disksOn3 = state
    if disksOn1:
        diskToMove = disksOn1[0]
        if not disksOn2 or disksOn2[0] > diskToMove:
            moves.append([1,2])
        if not disksOn3 or disksOn3[0] > diskToMove:
            moves.append([1,3])
    if disksOn2:
        diskToMove = disksOn2[0]
        if not disksOn1 or disksOn1[0] > diskToMove:
            moves.append([2,1])
        if not disksOn3 or disksOn3[0] > diskToMove:
            moves.append([2,3])
    if disksOn3:
        diskToMove = disksOn3[0]
        if not disksOn1 or disksOn1[0] > diskToMove:
            moves.append([3,1])
        if not disksOn2 or disksOn2[0] > diskToMove:
            moves.append([3,2])
    return moves

def makeMove(state, move):
    from copy import deepcopy
    stateNew = deepcopy(state)
    src,dest = move
    diskMoved = stateNew[src-1].pop(0)
    stateNew[dest-1].insert(0,diskMoved)
    return stateNew


def newStateRep(state):
    newrep = [0, 0, 0]
    for pegi, peglist in enumerate(state):
        for disk in peglist:
            newrep[disk-1] = pegi+1
    return newrep
	
def epsilonGreedy(Qnet, state, epsilon, validMovesF):
    moves = validMovesF(state)
    if np.random.uniform() < epsilon: # random move
        move = moves[random.sample(range(len(moves)),1)[0]]
        Q = Qnet.use(np.array([newStateRep(state) + move])) if Qnet.Xmeans is not None else 0
    else:                           # greedy move
        qs = []
        for m in moves:
            qs.append(Qnet.use(np.array([newStateRep(state) + m])) if Qnet.Xmeans is not None else 0)
        move = moves[np.argmax(qs)]
        Q = np.max(qs)
    return move, Q
	
def trainQnet(nReps, hiddenLayers, nIterations, nReplays, epsilon, epsilonDecayFactor, validMovesF, makeMoveF):
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
        move, _ = epsilonGreedy(Qnet, state, epsilon, validMovesF)
 
        while not done:
            step += 1
            
           # Make this move to get to nextState
            stateNext = makeMoveF(state, move)
            r = -1
            # Choose move from nextState
            moveNext, Qnext = epsilonGreedy(Qnet, stateNext, epsilon, validMovesF)
 
            if len(stateNext[2]) == 3:
                # goal found
                Qnext = 0
                done = True
                outcomes[rep] = step
                if rep%10 == 0 or rep == nReps-1:
                    print('rep={:d} epsilon={:.3f} steps={:d}'.format(rep,epsilon, int(outcomes[rep])), end=', ')
               
            samples.append([*newStateRep(state), *move, r, Qnext])
            samplesNextStateForReplay.append([*newStateRep(stateNext), *moveNext])

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
	
def main():
	hiddenLayers = [40]
	nReplays = 0
	nIterations = 10
	epsilon = 0.5
	epsilonDecayFactor = 0.99
	nReplays = 0
	Qnet, outcomes, samples = trainQnet(300, hiddenLayers, nIterations, nReplays, 
                                    epsilon, epsilonDecayFactor, validMoves, makeMove)
    
    
if __name__ == "__main__":
    main()
