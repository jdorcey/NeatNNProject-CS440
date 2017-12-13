import random

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

#Used for computing tile indices
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

class TwentyFortyEight:
    #2048 game puzzle
    def __init__(self):
        self.state = [[0 for col in range(4)] for row in range(4)]
        self.goalState = False
        random.seed(1337)
=======
>>>>>>> 2b40a402dc4fa328ca27ca993656185a217e3ea7
        self.randomTile()
        self.moves = 0
        self.currentScore = 0
        self.highScore = 0
<<<<<<< HEAD
=======
       
>>>>>>> 2b40a402dc4fa328ca27ca993656185a217e3ea7
        #Inital row dictionary
        self.initial = {
            UP : [[0, tile] for tile in range(4)],
            DOWN : [[3, tile] for tile in range(4)],
            LEFT : [[tile, 0] for tile in range(4)],
            RIGHT : [[tile, 3] for tile in range (4)]
        }

    #Merge the rows so the games state can be updated
    def mergeRow(self, row):
        nonzeros = []
        newRow = []
        merged = False

        #Move all non-zero tiles to the left and append 0's
        for tile in row:
            if tile != 0:
                nonzeros.append(tile)

        while len(nonzeros) != len(row):
            nonzeros.append(0)

        #Double tile value if neighbor has same value
        for tile in range(0, len(nonzeros) - 1):
            if nonzeros[tile] == nonzeros[tile + 1] and merged == False:
                newRow.append(2 * nonzeros[tile])
                self.currentScore += 2 * nonzeros[tile]
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

    #Prints game state
    def __repr__(self):
        for row in range(0, 4):
            print(self.state[row])

        return ""

    #Returns a list of legal moves the current game state can make
    def validMoves(self):
        moves = []

        for row in range(1, 4):
            for col in range(0,4):
                if self.state[row][col] == self.state[row -1][col] and [1] not in moves:
                    moves.append([1])
                if self.state[row -1][col] == 0 and [1] not in moves:
                    moves.append([1])

        for row in range(0, 3):
            for col in range(0,4):
                if self.state[row][col] == self.state[row +1][col] and [2] not in moves:
                    moves.append([2])
                if self.state[row +1][col] == 0 and [2] not in moves:
                    moves.append([2])

        for row in range(0, 4):
            for col in range(1,4):
                if self.state[row][col] == self.state[row][col -1] and [3] not in moves:
                    moves.append([3])
                if self.state[row][col -1] == 0 and [3] not in moves:
                    moves.append([3])

        for row in range(0, 4):
            for col in range(0,3):
                if self.state[row][col] == self.state[row][col +1] and [4] not in moves:
                    moves.append([4])
                if self.state[row][col +1] == 0 and [4] not in moves:
                    moves.append([4])

        if len(moves) != 0 :
            return moves
        else:
            moves.append([0])
            return moves

    #How the games current state gets updated
    def makeMove(self, movelist):
        move = movelist[0]
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
        #Move the rows columns to the left
        beforeMove = str(self.state)

        for element in initial:
            temp.append(element)
            row = []

            for i in range(1, 4):
                temp.append([x + y for x, y in zip(temp[-1], OFFSETS[move])])

            for i in temp:
                row.append(self.state[i[0]][i[1]])

            #Merge row
            merged = self.mergeRow(row)

            for x, y in zip(merged, temp):
                self.state[y[0]][y[1]] = x

            temp = []

        afterMove = str(self.state)
        if beforeMove != afterMove:
            self.moves += 1
            self.randomTile()

    #Add a new tile to game state, should be a 2 90% and a 4 10% of the time
    def randomTile(self):
        positions = []
        for row in range(4):
            for col in range(4):
                if self.state[row][col] == 0:
                    positions.append([row, col])

        #Select a random open tile
        randomT = random.choice(positions)
        choices = [(2, 9), (4, 1)]
        population = [v for v, c in choices for i in range(c)]
        tile = random.choice(population)
        self.state[randomT[0]][randomT[1]] = tile

    #Check if game is over
    def gameOver(self):
        for row in range(len(self.state)):
            for col in range(len(self.state[row])):
                if self.state[row][col] == 2048:
                    self.goalState = True
              
        check = self.validMoves() 
        if not check or self.goalState:
=======
        if check[0] == [0] or self.goalState:
>>>>>>> 2b40a402dc4fa328ca27ca993656185a217e3ea7
            self.reset()
            return True
        else:
            return False
                
    #Returns the input size used by Neural Networks
    def inputSize(self):
        #there are always 16 tiles in the game + the move
        return 17

    #Reset game state so a new game can be played
    def reset(self):
        if self.highScore < self.currentScore:
            self.highScore = self.currentScore

        self.state = [[0 for col in range(4)] for row in range(4)]
        self.randomTile()
        self.moves = 0
        self.currentScore = 0

    #Another way of representing the games state
    def newStateRep(self):
        newRep = []

        for c in range(len(self.state)):
            for i in range(len(self.state)):
                newRep.append(self.state[c][i])

        return newRep

    # Returns all the moves that can be made in the game
    def allMoves(self):
        return [[1], [2], [3], [4]]

    # Determines the fitness to be used by the training algorithm
    def fitness(self):
        score = 0
        for row in self.state:
            for element in row:
                if element >= score:
                    score = element
        return score
    
    def getOptimal(self):
        return 2048
