from Box import Box
from Position import Postion

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

    def getBox(self,postion):
        if(postion.row>=self.board_length or postion.column>=self.board_length):
            return None
        else:
            return self.board[postion.row][postion.column]

    '''
    loads the used box position in valid_positions
    '''            
    def loadValidPositions(self):
        self.valid_positions = []

        # first row
        self.valid_positions.append(Postion(0, 0))
        self.valid_positions.append(Postion(0, 3))
        self.valid_positions.append(Postion(0, 6))

        # second row
        self.valid_positions.append(Postion(1, 1))
        self.valid_positions.append(Postion(1, 3))
        self.valid_positions.append(Postion(1, 5))

        # third row
        self.valid_positions.append(Postion(2, 2))
        self.valid_positions.append(Postion(2, 3))
        self.valid_positions.append(Postion(2, 4))

        # fourth row
        self.valid_positions.append(Postion(3, 0))
        self.valid_positions.append(Postion(3, 1))
        self.valid_positions.append(Postion(3, 2))
        self.valid_positions.append(Postion(3, 4))
        self.valid_positions.append(Postion(3, 5))
        self.valid_positions.append(Postion(3, 5))
        self.valid_positions.append(Postion(3, 6))

        # fifth row
        self.valid_positions.append(Postion(4, 2))
        self.valid_positions.append(Postion(4, 3))
        self.valid_positions.append(Postion(4, 4))

        # sixth row
        self.valid_positions.append(Postion(5, 1))
        self.valid_positions.append(Postion(5, 3))
        self.valid_positions.append(Postion(5, 5))

        # seventh row
        self.valid_positions.append(Postion(6, 0))
        self.valid_positions.append(Postion(6, 3))
        self.valid_positions.append(Postion(6, 6))
        
    '''
    making the some of the boxes as usable boxes
    '''
    def loadDefaultBoard(self):

        for poistion in self.valid_positions:
            box = self.board[poistion.row][poistion.column]
            # making this box can be used one
            box.updateIsAllowed()

#b1 = Board()
#b1.displayBoard()
