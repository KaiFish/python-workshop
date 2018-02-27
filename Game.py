from Board import Board

class Game:
    def __init__(self):
        self.board = Board()

    def check3(self, three):
        if three[0] == three[1] and three[1] == three[2]:
            return True
        else:
            return False

    def checkWin(self):
        row0 = self.board.getRow(0)
        row1 = self.board.getRow(1)
        row2 = self.board.getRow(2)
        col0 = self.board.getCol(0)
        col1 = self.board.getCol(1)
        col2 = self.board.getCol(2)
        diag1 = self.board.getDiag(1)
        diag2 = self.board.getDiag(2)

        if self.check3(row0):
            return True
        elif self.check3(row1):
            return True
        elif self.check3(row2):
            return True
        elif self.check3(col0):
            return True
        elif self.check3(col1):
            return True
        elif self.check3(col2):
            return True
        elif self.check3(diag1):
            return True
        elif self.check3(diag2):
            return True
        else:
            return False

    def changeBoard(self, player, move):
        if move[0] != 0 or move[0] != 1 or move[0] != 2 or move[1] != 0 or move[1] != 1 or move[1] != 2:
            print("error")
        else:
            row = self.board.getRow[move[0]]
            row[move[1]] = player
            self.board = self.board.switchRow(move[0], row)
        return

    def turn(self, player):
        print("It is player " + str(player) + "'s turn'")
        row = input("which row would you like?")
        row = int(row)
        col = input("which column would you like?")
        col = int(col)
        self.changeBoard(player, [row, col])
        return
