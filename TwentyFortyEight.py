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
  
#Move all non-zero tiles to the left 
def mergeRow(row):
    nonzeros = []
    newRow = []
    merged = False
    
    for tile in row:
        if tile != 0:
            nonzeros.append(tile)

    while len(nonzeros) != len(row):
        nonzeros.append(0)
        
    #Double tiles
    for tile in range(0, len(nonzeros) - 1):
        merged = False
        if nonzeros[tile] == nonzeros[tile + 1] and merged == False:
            newRow.append(2 * nonzeros[tile])
            merged = True
        elif nonzeros[tile] != nonzeros[tile + 1] and merged == False:
            newRow.append(nonzeros[tile])
    
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
            
    # Print game grid
    def __str__(self):
        for row in range(0, 4):
            print(self.state[row])
        return ""
    
    def ValidMoves(self):
        moves = []
        for row in range(0, 3):
            for col in range(0,3):
                if self.state[row][col] == self.state[row -1][col] and 1 not in moves:
                    moves.append(1)
                if self.state[row][col] == self.state[row +1][col] and 2 not in moves:
                    moves.append(2)
                if self.state[row][col] == self.state[row][col -1] and 3 not in moves:
                    moves.append(3)
                if self.state[row][col] == self.state[row][col +1] and 4 not in moves:
                    moves.append(4)
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
        before = str(self.state)

        for element in initial:
            temp.append(element)
            indices = []

            for index in range(1, 4):
                temp.append([x + y for x, y in zip(temp[-1], OFFSETS[move])])
            
            for index in temp:
                indices.append(self.state[index[0]][index[1]])
            
            merged = mergeRow(indices)       
            for x, y in zip(merged, temp):
                self.state[y[0]][y[1]] = x
        
            temp = []    
        after = str(self.state)
        
        if before != after:
            self.randomTile()       

    # Create new tile in randomly selected spot, should be 2 90% of the time
    #and 4 10% of the time      
    def randomTile(self):
        if not self.gameover():
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
        else:
            print("GAME OVER")
            self.reset()
            
    #check if game is over
    def gameover(self):
        positions = []
        for row in range(4):
            for col in range(4):
                if self.state[row][col] == 0:
                    positions.append([row, col])
        if positions:
            return False
        else:
            return True
        
    #Reset game so grid is empty
    def reset(self):
        self.state = [[0 for col in range(4)] for row in range(4)]
    
