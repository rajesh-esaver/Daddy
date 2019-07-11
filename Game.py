from Player import Player
from Board import Board
from Position import Position
from Move import Move

class Game:
    def __init__(self,p1_symbol="1",p2_symbol="2"):
        self.board = Board()
        self.player_1 = Player(self.board,p1_symbol)
        self.player_2 = Player(self.board,p2_symbol)

    def readPosition(self):
        while(True):
            row,column = map(int,input().split(" "))
            if(row<0 or row>6 or column<0 or column>6):
                print("not valid row and column, please enter it again")
                continue
            return Position(row,column)

    def readPlaceCoinPosition(self):
        # assumed user will give the input separated by space
        print("Enter a Position(row,column) to place the coin")
        return self.readPosition()

    def readPositionForOpponentCoinRemove(self):
        print("Enter a Position(row,column) of opponent coin to remove")
        return self.readPosition()

    def readMove(self):
        print("Need to enter both source and destination positions")
        print("Enter source Position(row,column)")
        src_position = self.readPosition()
        print("Enter destination Position(row,column)")
        dst_position = self.readPosition()
        return Move(src_position,dst_position)

    def declaerWinner(self,win_player):
        print("Player "+win_player.player_symbol+" has won the GAME !!")

    def displayPlayerInfo(self,player):
        print("Current Player Symbol is "+player.player_symbol)

    def displayGameInfo(self):
        self.board.displayBoard()
        if(self.player_1.times_can_place_coin>0 or self.player_2.times_can_place_coin>0):
            print("Player " + self.player_1.player_symbol + ", can place coin: " + str(self.player_1.times_can_place_coin)+" times")
            print("Player " + self.player_2.player_symbol + ", can place coin: " + str(self.player_2.times_can_place_coin)+" times")
        print("Player "+self.player_1.player_symbol+", remaining coins: "+str(self.player_1.no_of_coins))
        print("Player " + self.player_2.player_symbol + ", remaining coins: " + str(self.player_2.no_of_coins))

game = Game()
curr_player = game.player_1
opponent_player = game.player_2
game.displayGameInfo()

while(True):
    if(curr_player.times_can_place_coin>0 and curr_player.no_of_coins>0):
        game.displayPlayerInfo(curr_player)
        while(True):
            position = game.readPlaceCoinPosition()
            ret_val = curr_player.placeCoin(position)
            status,msg = ret_val[0],ret_val[1]
            if(status):
                ret_val = curr_player.checkIfItIsDaddyForPosition(position)
                status, msg = ret_val[0], ret_val[1]
                if(status):
                    # it's a daddy you can remove opponent coin
                    game.displayGameInfo()
                    print(msg)
                    # check if there is valid position to remove opponents coin
                    ret_val = curr_player.checkIfThereIsValidCoinToRemove(opponent_player)
                    status, msg = ret_val[0], ret_val[1]
                    if(status):
                        while(True):
                            rem_position = game.readPositionForOpponentCoinRemove()
                            ret_val = curr_player.removeOpponentsCoin(opponent_player,rem_position)
                            status, msg = ret_val[0], ret_val[1]
                            if(status):
                                break
                            else:
                                print(msg)
                    else:
                        print(msg)
                break
            else:
                print(msg)
    else:
        # need to check if there is valid position to move
        game.displayPlayerInfo(curr_player)
        if(curr_player.no_of_coins>2):
            # check if there is valid position to make move
            ret_val = curr_player.checkIsThereValidCoinToMakeMove()
            status, msg = ret_val[0], ret_val[1]
            if(status):
                while (True):
                    move = game.readMove()
                    ret_val = curr_player.moveCoin(move)
                    status, msg = ret_val[0], ret_val[1]
                    if(status):
                        ret_val = curr_player.checkIfItIsDaddyForMove(move)
                        status, msg = ret_val[0], ret_val[1]
                        if(status):
                            # it's a daddy you can remove opponent coin
                            game.displayGameInfo()
                            print(msg)
                            # check if there is valid position to remove opponents coin
                            ret_val = curr_player.checkIfThereIsValidCoinToRemove(opponent_player)
                            status, msg = ret_val[0], ret_val[1]
                            if(status):
                                while(True):
                                    rem_position = game.readPositionForOpponentCoinRemove()
                                    ret_val = curr_player.removeOpponentsCoin(opponent_player,rem_position)
                                    status, msg = ret_val[0], ret_val[1]
                                    if (status):
                                        break
                                    else:
                                        print(msg)
                            else:
                                print(msg)
                        break
                    else:
                        print(msg)
            else:
                print(msg)
        else:
            # curr_player don't have enough coins to make daddy, so opponent_player wins
            game.declaerWinner(opponent_player)
            break
    game.displayGameInfo()
    if(curr_player==game.player_1):
        curr_player = game.player_2
        opponent_player = game.player_1
    else:
        curr_player = game.player_1
        opponent_player = game.player_2
