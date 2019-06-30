from Box import Box
from Position import Postion

class Board:
    def __init__(self):
        self.board_length = 7
        self.board = [[Box() for _ in range(self.board_length)] for _ in range(self.board_length)]
        self.loadDefaultBoard()

    def displayBoard(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                box = self.board[row][col]
                print_symbol = "O" if box.is_allowed else "-"
                print(print_symbol,end=" ")
            print("\n")

    '''
    making the some of the boxes as usable boxes
    '''
    def loadDefaultBoard(self):
        boxes_to_use = []

        # first row
        boxes_to_use.append(Postion(0, 0))
        boxes_to_use.append(Postion(0, 3))
        boxes_to_use.append(Postion(0, 6))

        # second row
        boxes_to_use.append(Postion(1, 1))
        boxes_to_use.append(Postion(1, 3))
        boxes_to_use.append(Postion(1, 5))

        # third row
        boxes_to_use.append(Postion(2, 2))
        boxes_to_use.append(Postion(2, 3))
        boxes_to_use.append(Postion(2, 4))

        # fourth row
        boxes_to_use.append(Postion(3, 0))
        boxes_to_use.append(Postion(3, 1))
        boxes_to_use.append(Postion(3, 2))
        boxes_to_use.append(Postion(3, 4))
        boxes_to_use.append(Postion(3, 5))
        boxes_to_use.append(Postion(3, 5))
        boxes_to_use.append(Postion(3, 6))

        # fifth row
        boxes_to_use.append(Postion(4, 2))
        boxes_to_use.append(Postion(4, 3))
        boxes_to_use.append(Postion(4, 4))

        # sixth row
        boxes_to_use.append(Postion(5, 1))
        boxes_to_use.append(Postion(5, 3))
        boxes_to_use.append(Postion(5, 5))

        # seventh row
        boxes_to_use.append(Postion(6, 0))
        boxes_to_use.append(Postion(6, 3))
        boxes_to_use.append(Postion(6, 6))

        for poistion in boxes_to_use:
            box = self.board[poistion.row][poistion.column]
            # making this box can be used one
            box.updateisAllowed()
