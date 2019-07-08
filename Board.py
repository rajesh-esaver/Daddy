from Box import Box
from Position import Position

class Board:
    def __init__(self):
        self.board_length = 7
        self.coins_for_daddy = 3
        self.board = [[Box() for _ in range(self.board_length)] for _ in range(self.board_length)]
        self.valid_positions = []
        self.loadValidPositions()
        self.loadDefaultBoard()

    def displayBoard(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                box = self.board[row][col]
                print_symbol = (box.symbol if box.symbol else "O") if box.is_allowed else "-"
                print(print_symbol,end=" ")
            print("")

    def getBox(self,Position):
        if(Position.row>=self.board_length or Position.column>=self.board_length):
            return None
        else:
            return self.board[Position.row][Position.column]

    def getBoxFromRowAndColumn(self,row,column):
        if(row>=self.board_length or column>=self.board_length):
            return None
        else:
            return self.board[row][column]

    '''
    loads the used box position in valid_positions
    '''            
    def loadValidPositions(self):
        self.valid_positions = []

        # first row
        self.valid_positions.append(Position(0, 0))
        self.valid_positions.append(Position(0, 3))
        self.valid_positions.append(Position(0, 6))

        # second row
        self.valid_positions.append(Position(1, 1))
        self.valid_positions.append(Position(1, 3))
        self.valid_positions.append(Position(1, 5))

        # third row
        self.valid_positions.append(Position(2, 2))
        self.valid_positions.append(Position(2, 3))
        self.valid_positions.append(Position(2, 4))

        # fourth row
        self.valid_positions.append(Position(3, 0))
        self.valid_positions.append(Position(3, 1))
        self.valid_positions.append(Position(3, 2))
        self.valid_positions.append(Position(3, 4))
        self.valid_positions.append(Position(3, 5))
        self.valid_positions.append(Position(3, 5))
        self.valid_positions.append(Position(3, 6))

        # fifth row
        self.valid_positions.append(Position(4, 2))
        self.valid_positions.append(Position(4, 3))
        self.valid_positions.append(Position(4, 4))

        # sixth row
        self.valid_positions.append(Position(5, 1))
        self.valid_positions.append(Position(5, 3))
        self.valid_positions.append(Position(5, 5))

        # seventh row
        self.valid_positions.append(Position(6, 0))
        self.valid_positions.append(Position(6, 3))
        self.valid_positions.append(Position(6, 6))
        
    '''
    making the some of the boxes as usable boxes
    '''
    def loadDefaultBoard(self):
        for poistion in self.valid_positions:
            box = self.board[poistion.row][poistion.column]
            # making this box can be used one
            box.updateIsAllowed()

# b1 = Board()
# b1.displayBoard()
