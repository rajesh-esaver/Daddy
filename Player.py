import Position
import Board
import Move
class Player:
    def __init__(self,board,symbol=1):
        self.no_of_coins = 9
        self.times_can_place_coin = self.no_of_coins
        self.board = board
        self.player_symbol = symbol

    def placeCoin(self,position):
        # checking basic validations
        if(self.times_can_place_coin<=0):
            return [False,"your all coins placed on the board, can't place any more coins"]
        box = self.board.getBox(position)
        if(box==None or box.isBoxAllowed()==False or box.isBoxAvailable()==False):
            return [False,"this is not a valid box to place your coin"]

        # update the box with current player symbol
        box.updateSymbol(self.player_symbol)

        # decrease the times_can_place_coin, since player placed the coin
        # TODO test it - self.times_can_place_coin -= 1
        self.reduceNoTimesCanMove(self)

        # decreasing the no_of_coins
        self.reduceCoin(self)

        return [True,"Placed Coin successfully"]

    def reduceCoin(self,player):
        if(player.no_of_coins>0):
            player.no_of_coins -= 1

    def reduceNoTimesCanMove(self,player):
        if(player.times_can_place_coin>0):
            player.times_can_place_coin -= 1

    '''
    this method checks if there is a Daddy exist for placed position
    '''
    def checkIfItIsDaddy(self,position):
        # check should happen for both column and row
        box = self.board.getBox(position)
        if(box==None):
            return [False,"Not a valid position"]

        # check row side
        if(self.checkDaddyInRow(position)):
            return [True,"Daddy in row"]

        # check column side
        if(self.checkDaddyInColumn(position)):
            return [True, "Daddy in column"]

        return [False,"No daddy at this juncture"]

    '''
    this method checks if there is a Daddy exist for moved coin
    '''
    def checkIfItIsDaddy(self,move):
        # check should happen for either column or row accordingly
        # assuming src_position and dst_position are valid
        src_position = move.src_position
        dst_position = move.dst_position

        row_diff = abs(src_position.row-dst_position.row)
        if(row_diff>0):
            # moved coin in the same column
            if(self.checkDaddyInRow(dst_position)):
                return [True, "Daddy in row"]
        else:
            # movied coin the the same row
            if(self.checkDaddyInColumn(dst_position)):
                return [True, "Daddy in column"]

        return [False,"No daddy at this juncture"]

    '''
    function for removing opponents coins
    '''
    def removeOpponentsCoin(self,opponent_player,position):
        box = self.board.getBox(position)
        if(box==None or box.isBoxAllowed()==False or box.symbol==self.player_symbol):
            return [False, "this is not a valid box to remove your opponent coin"]

        # TODO check that coin to be removed is not in Daddy
        # TODO is there valid opponent coin that can be removed

        # making the box as empty
        box.updateSymbol()

        # reducing the number of coins for the opponent player
        self.reduceCoin(opponent_player)

        return [True,"Coin removed successfully"]

    '''
    function for moving the player coin
    '''
    def moveCoin(self,move):
        src_position = move.src_position
        dst_position = move.dst_position

        src_box = self.board.getBox(src_position)
        dst_box = self.board.getBox(dst_position)

        if(src_box==None or src_box.isBoxAllowed()==False or src_box.symobl!=self.player_symbol):
            return [False, "this is not a valid source box position"]

        if (dst_box == None or dst_box.isBoxAllowed()==False or dst_box.isBoxAvailable()==False):
            return [False, "this is not a valid destination box position"]

        if(src_box==dst_position):
            return [False,"Source and Destination should not be same"]

        # TODOcheck check diff btw src and dst is one
        row_diff = abs(src_position.row - dst_position.row)
        if (row_diff > 0):
            # moved coin in the same column
            if (not self.checkDstIsNextValidBoxInColumn(move)):
                return [False, "this is not a valid destination box position"]
        elif(row_diff==0):
            # movied coin the the same row
            if(not self.checkDstIsNextValidBoxInRow(move)):
                return [False,"this is not a valid destination box position"]
        else:
            return [False, "this is not a valid source and destination box positions"]

        # remove the coin from current box and add the coin in destination
        src_box.updateSymbol()
        dst_box.updateSymbol(self.player_symbol)

        return [True, "Coin moved successfully"]


    '''
    check whether destination position is next valid position from source in row
    '''
    def checkDstIsNextValidBoxInRow(self,move):
        src_position = move.src_position
        dst_position = move.dst_position

        curr_row = src_position.row

        # if it is middle row, src and dst should be either <3 or >3 in the row
        if(curr_row==3):
            if(src_position.column<3 and dst_position.column<3):
                pass
            elif(src_position.column>3 and dst_position.column>3):
                pass
            else:
                False

        if(src_position.column < dst_position.column):
            # moved forward in the row
            for curr_col in range(src_position.column+1,self.board.board_length):
                curr_box = self.board.getBox(curr_row,curr_col)
                if(curr_box.isBoxAllowed()):
                    if(curr_box.isBoxAvailable() and dst_position.column==curr_col):
                        return True
                    else:
                        return False
        elif(dst_position.column < src_position.column):
            # moved backward in the row
            for curr_col in range(src_position.column - 1,-1,-1):
                curr_box = self.board.getBox(curr_row, curr_col)
                if (curr_box.isBoxAllowed()):
                    if (curr_box.isBoxAvailable() and dst_position.column == curr_col):
                        return True
                    else:
                        return False
        else:
            return False
        return False

    '''
    check whether destination position is next valid position from source in column
    '''
    def checkDstIsNextValidBoxInColumn(self,move):
        src_position = move.src_position
        dst_position = move.dst_position

        curr_col = src_position.column

        # if it is middle column, src and dst should be either <3 or >3 in the column
        if (curr_col == 3):
            if(src_position.row < 3 and dst_position.row < 3):
                pass
            elif(src_position.row > 3 and dst_position.row > 3):
                pass
            else:
                False

        if(src_position.row < dst_position.row):
            # moved forward in the column
            for curr_row in range(src_position.row + 1, self.board.board_length):
                curr_box = self.board.getBox(curr_row, curr_col)
                if (curr_box.isBoxAllowed()):
                    if (curr_box.isBoxAvailable() and dst_position.row == curr_row):
                        return True
                    else:
                        return False
        elif(dst_position.row < src_position.row):
            # moved backward in the column
            for curr_row in range(src_position.row - 1,-1,-1):
                curr_box = self.board.getBox(curr_row, curr_col)
                if (curr_box.isBoxAllowed()):
                    if (curr_box.isBoxAvailable() and dst_position.row == curr_row):
                        return True
                    else:
                        return False
        else:
            return False
        return False


    '''
    checking for daddy in row
    '''
    def checkDaddyInRow(self,position):
        count = 0
        # since in row 3 total 6 coins can be there
        if(position.row!=3):
            for i in range(0, self.board.board_length):
                box_in_row = self.board[position.row][i]
                if (box_in_row != None and box_in_row.symbol == self.player_symbol):
                    count += 1
        else:
            if(position.column<=3):
                i = 0
                n = 3
            else:
                i = 4
                n = self.board.board_length
            for i in range(i,n):
                box_in_row = self.board[position.row][i]
                if (box_in_row != None and box_in_row.symbol == self.player_symbol):
                    count += 1

        if(count == self.board.coins_for_daddy):
            return True
        else:
            return False

    '''
    checking for daddy in column
    '''
    def checkDaddyInColumn(self,position):
        count = 0
        if (position.column != 3):
            for i in range(0, self.board.board_length):
                box_in_col = self.board[i][position.column]
                if (box_in_col != None and box_in_col.symbol == self.player_symbol):
                    count += 1
        else:
            if (position.row <= 3):
                i = 0
                n = 3
            else:
                i = 4
                n = self.board.board_length
            for i in range(i, n):
                box_in_col = self.board[i][position.column]
                if (box_in_col != None and box_in_col.symbol == self.player_symbol):
                    count += 1

        if (count == self.board.coins_for_daddy):
            return True
        else:
            return False
