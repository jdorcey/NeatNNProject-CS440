# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:25:14 2017

@author: Tom Shaw
"""
from copy import deepcopy

class TOH: #towers of Hanoi puzzle
    def __init__(self):
        self.state = [[1,2,3],[],[]]
        
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
        return stateNew
    
    def newStateRep(self):
        newrep = [0, 0, 0]
        for pegi, peglist in enumerate(self.state):
            for disk in peglist:
                newrep[disk-1] = pegi+1
        return newrep
    
    
