# -*- coding: utf-8 -*-
#@author: Jennifer Dorcey

import random     

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

#Offsets for computing tile indices in each direction    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
  
def mergeRow(row):
    nonzeros = []
    newRow = []
    merged = False
    
    #Move all non-zero tiles to the left and append 0's
    for tile in row:
        if tile != 0:
            nonzeros.append(tile)

    while len(nonzeros) != len(row):
        nonzeros.append(0)
             
    #Double tile is neighbor is same value   
    for tile in range(0, len(nonzeros) - 1):
        if nonzeros[tile] == nonzeros[tile + 1] and merged == False:
            newRow.append(2 * nonzeros[tile])
            merged = True
        elif nonzeros[tile] != nonzeros[tile + 1] and merged == False:
            newRow.append(nonzeros[tile])
        elif merged == True:
            merged = False

    if nonzeros[-1] != 0 and merged == False:
        newRow.append(nonzeros[-1])
        
    while len(newRow) != len(nonzeros):
        newRow.append(0)

    return newRow

class TwentyFortyEight:

    def __init__(self):
        self.state = []
        self.reset()

        #Inital row dictionary
        self.initial = {
            UP : [[0, tile] for tile in range(4)],
            DOWN : [[3, tile] for tile in range(4)],
            LEFT : [[tile, 0] for tile in range(4)],
            RIGHT : [[tile, 3] for tile in range (4)]
        }
            
    # Print game 
    def __str__(self):
        for row in range(0, 4):
            print(self.state[row])
        return ""
    
    def validMoves(self):
        moves = []
        
        for row in range(1, 4):
            for col in range(0,4):
                if self.state[row][col] == self.state[row -1][col] and 1 not in moves:
                    moves.append(1)
                if self.state[row -1][col] == 0 and 1 not in moves:
                    moves.append(1)
                    
        for row in range(0, 3):
            for col in range(0,4):
                if self.state[row][col] == self.state[row +1][col] and 2 not in moves:
                    moves.append(2)
                if self.state[row +1][col] == 0 and 2 not in moves:
                    moves.append(2)
        
        for row in range(0, 4):
            for col in range(1,4):
                if self.state[row][col] == self.state[row][col -1] and 3 not in moves:
                    moves.append(3)
                if self.state[row][col -1] == 0 and 3 not in moves:
                    moves.append(3)
                    
        for row in range(0, 4):
            for col in range(0,3):          
                if self.state[row][col] == self.state[row][col +1] and 4 not in moves:
                    moves.append(4)
                if self.state[row][col +1] == 0 and 4 not in moves:
                    moves.append(4)  
              
        if self.gameOver(moves):
            print("NO MORE MOVES! GAME OVER, RESETTING GAME!")
            return self.reset()
        else:
            return moves
    
    # Move tiles in the given direction and add new tile if any tiles moved
    def makeMove(self, move):
        initial = self.initial[move]
        temp = []     
        
        if(move == UP):
            self.moveHelper(initial, move, temp)
        elif(move == DOWN):
            self.moveHelper(initial, move, temp)
        elif(move == LEFT):
            self.moveHelper(initial, move, temp)
        elif(move == RIGHT):
            self.moveHelper(initial, move, temp)
            
    def moveHelper(self, initial, move, temp):
        # Move all columns and merge
        beforeMove = str(self.state)

        for element in initial:
            temp.append(element)
            row = []

            for i in range(1, 4):
                temp.append([x + y for x, y in zip(temp[-1], OFFSETS[move])])
             
            for i in temp:
                row.append(self.state[i[0]][i[1]])

            merged = mergeRow(row)

            for x, y in zip(merged, temp):
                self.state[y[0]][y[1]] = x    
            temp = []  
            
        afterMove = str(self.state)
        if beforeMove != afterMove:
            self.randomTile()       

    # Create new tile in randomly selected spot, should be 2 90% of the time
    #and 4 10% of the time      
    def randomTile(self):
        positions = []
        for row in range(4):
            for col in range(4):
                if self.state[row][col] == 0:
                    positions.append([row, col])
        randomT = random.choice(positions)
        choices = [(2, 9), (4, 1)]
        population = [v for v, c in choices for i in range(c)]
        tile = random.choice(population)
        self.state[randomT[0]][randomT[1]] = tile
            
    #check if game is over
    def gameOver(self, moves):
        if len(moves) == 0:
            return True
        else:
            return False
        
    #Reset game so grid is empty
    def reset(self):
        self.state = [[0 for col in range(4)] for row in range(4)]
    
