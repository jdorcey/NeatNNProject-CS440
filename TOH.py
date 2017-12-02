# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:25:14 2017

@author: Tom Shaw
"""
from copy import deepcopy

class TOH: #towers of Hanoi puzzle
    def __init__(self, n=3):
        self.n = n
        self.state = [[1,2,3],[],[]]
        self.moves = 0
        #optimal moves calculation
        self.optimalMoves = ((2**n)-1)
        
    def __repr__(self):
        printState()
        return
        
    def printState(self):
        lens = [len(p) for p in self.state]
        for height in range(max(lens),0,-1):
            row = ""
            for p in range(3):
                if lens[p] >= height:
                    row += str(self.state[p][lens[p]-height]) + ' '
                else:
                    row += '  '
            print(row)
        print('------')
        print()
        
    def validMoves(self):
        """Given state like [[1,2,3],[],[]]
        return valid moves, like [(1,2),(1,3)]) pairs of source and dest peg"""
        moves = []
        disksOn1,disksOn2,disksOn3 = self.state
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
    
    def makeMove(self, move):
        from copy import deepcopy
        stateNew = deepcopy(self.state)
        src,dest = move
        diskMoved = stateNew[src-1].pop(0)
        stateNew[dest-1].insert(0,diskMoved)
        #increment number of moves made in this problem
        self.moves += 1
        return stateNew
    
    def goaltest(self):
        pass
    
    def percentCorrect(self):
        #pecent complete is how many disks there are on the goal peg over the total number
        return len(self.state[2])/self.n
    
    #fitness should be called on a state after NN has run on it
    #this function will determine the fitness to be used by the training algorithm
    def fitness(self):
        score = 0
        #max score is 1100
        if(goaltest()):
            #if game completed add 100 points
            #will automatically make a network that completes the game more fit
            #than a network that hasn't finished
            score +=100 
            #higher fitness for less moves moves
            #max score for optimal moves
            score += (optimalMoves/actualMoves) * 1000 
        else:
            #if game hasn't completed determine how 
            score += percentCorrect()*100
        return score
