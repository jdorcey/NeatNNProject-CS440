from copy import deepcopy

class TOH:
    #Towers of Hanoi game puzzle
    def __init__(self, n = 3):
        self.n = n
        numDisks = []
        for i in range(1, n + 1):
            numDisks.append(i)
        self.state = [numDisks,[],[]]
        self.goalState = [[],[], numDisks]
        self.moves = 0
        #optimal moves calculation
        self.optimalMoves = ((2**n)-1)

    #Prints game state
    def __repr__(self):
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

        return ""

    #Returns a list of legal moves the current game state can make
    def validMoves(self):
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

    #How the current game state changes
    def makeMove(self, move):
        stateNew = deepcopy(self.state)
        src,dest = move
        diskMoved = stateNew[src-1].pop(0)
        stateNew[dest-1].insert(0,diskMoved)
        #increment number of moves made in this problem
        self.moves += 1
        self.state = stateNew

        return self.state

    #Check if game is over
    def gameOver(self):
        if(self.state == self.goalState):
            self.reset()
            return True

        return False

    #Returns the input size used by Neural Networks
    def inputSize(self):
        #how many disks are being used + move
        return self.n + 2

    #Another way of representing the games state
    def newStateRep(self):
        newRep = []
        for i in range(1, self.n + 1):
            newRep.append(0)

        for pegi, peglist in enumerate(self.state):
            for disk in peglist:
                newRep[disk - 1] = pegi + 1

        return newRep

    #Reset game state so a new game can be played
    def reset(self):
        numDisks = []
        for i in range(1, self.n + 1):
            numDisks.append(i)

        self.state = [numDisks, [], []]
        self.moves = 0

    # Returns all the moves that can be made in the game
    def allMoves(self):
        return [[1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [3, 2]]

    # Calculates how close the game is to being completed
    def percentCorrect(self):
        # How many disks there are on the goal peg/ the total number of disks
        return len(self.state[2]) / self.n

    # Determines the fitness to be used by the training algorithm
    def fitness(self):
        # fitness should be called on a state after NN has run on it
        score = 0
        # max score is 1100
        if self.gameOver():
            # if game completed add 100 points
            # will automatically make a network that completes the game more fit
            # than a network that hasn't finished
            score += 100
            # higher fitness for less moves moves
            # max score for optimal moves
            score += (self.optimalMoves / self.moves) * 10000
        else:
            # if game hasn't completed determine how
            score += self.percentCorrect() * 100 + self.thirdPeg()
        return score
    
    def thirdPeg(self):
        bonus = 0
        if 3 in self.state[2]:
            bonus += 10
        if 2 in self.state[2]:
            bonus += 2
        return bonus
    
    def getOptimal(self):
        return 11000
