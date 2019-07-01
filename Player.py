import Position
import Board
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

        self.checkIfItIsDaddy(position)

    def reduceCoin(self,player):
        if(player.no_of_coins>0):
            player.no_of_coins -= 1

    def reduceNoTimesCanMove(self,player):
        if(player.times_can_place_coin>0):
            player.times_can_place_coin -= 1

    '''
    this method checks if there is a Daddy exist for placed postion
    '''
    def checkIfItIsDaddy(self,position):
        #TODO check should happen for both column and row in Position
        pass

    '''
    this method checks if there is a Daddy exist for moved coin
    '''
    def checkIfItIsDaddy(self, src_position,dst_position):
        # TODO check should happend for either column or row accordingly
        pass

    '''
    function for removing opponents coins
    '''
    def removeOpponentsCoin(self,opponent_player,position):
        box = self.board.getBox(position)
        if(box==None or box.isBoxAllowed()==False or box.symbol==self.player_symbol):
            return [False, "this is not a valid box to remove your opponent coin"]

        # making the box as empty
        box.updateSymbol()

        # reducing the number of coins for the opponent player
        self.reduceCoin(opponent_player)

        return [True,"Coin removed successfully"]

    '''
    function for moving the player coin
    '''
    def moveCoin(self,src_position,dst_position):
        pass

