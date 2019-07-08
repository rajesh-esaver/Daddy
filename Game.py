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
        row,column = map(int,input().split(" "))
        return Position(row,column)

    def readPlaceCoinPosition(self):
        # assumed user will give the input separated by space
        print("Enter a Position(row,column) to place the coin")
        return self.readPosition()

    def readPositionForOpponentCoinRemove(self):
        print("Enter a Position(row,column) of opponent coin to remove")
        return self.readPosition()

    def readMove(self):
        # TODO loop this until got the valid move
        src_position = self.readPosition()
        dst_position = self.readPosition()
        return Move(src_position,dst_position)

    def declaerWinner(self,win_player):
        print(win_player.player_symbol+" has won the GAME !!")

    def displayPlayerInfo(self,player):
        print("Current Player Symbol is "+player.player_symbol)

game = Game()
curr_player = game.player_1
opponent_player = game.player_2
game.board.displayBoard()

while(True):
    if(curr_player.times_can_place_coin>0):
        game.displayPlayerInfo(curr_player)
        while(True):
            position = game.readPlaceCoinPosition()
            ret_val = curr_player.placeCoin(position)
            status,msg = ret_val[0],ret_val[1]
            if(status):
                if(curr_player.checkIfItIsDaddyForPosition(position)[0]):
                    # it's a daddy you can remove opponent coin
                    while(True):
                        rem_position = game.readPositionForOpponentCoinRemove()
                        ret_val = curr_player.removeOpponentsCoin(opponent_player,rem_position)
                        status, msg = ret_val[0], ret_val[1]
                        if(status):
                            break
                        else:
                            print(msg)
                break
            else:
                print(msg)
    else:
        # need to check if there is valid position to move
        game.displayPlayerInfo(curr_player)
        if(curr_player.no_of_coins>2):
            while (True):
                move = game.readMove()
                ret_val = curr_player.moveCoin(move)
                status, msg = ret_val[0], ret_val[1]
                if(status):
                    if(curr_player.checkIfItIsDaddyForMove(move)[0]):
                        # it's a daddy you can remove opponent coin
                        while(True):
                            rem_position = game.readPositionForOpponentCoinRemove()
                            ret_val = curr_player.removeOpponentsCoin(opponent_player,rem_position)
                            status, msg = ret_val[0], ret_val[1]
                            if (status):
                                break
                            else:
                                print(msg)
                    break
                else:
                    print(msg)
        else:
            # curr_player don't have enough coins to make daddy, so opponent_player wins
            game.declaerWinner(opponent_player)
            break
    game.board.displayBoard()
    if(curr_player==game.player_1):
        curr_player = game.player_2
        opponent_player = game.player_1
    else:
        curr_player = game.player_1
        opponent_player = game.player_2
