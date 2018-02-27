class Board:
    def __init__(self):
        self.row0 = [0, 0, 0]
        self.row1 = [0, 0, 0]
        self.row2 = [0, 0, 0]
        self.board = [self.row0, self.row1, self.row2]

    def printBoard(self):
        print(str(self.board[0]) + '\n' + str(self.board[1]) + '\n' + str(self.board[2]))

    def getRow(self, num):
        if num == 0:
            return self.row0
        if num == 1:
            return self.row1
        if num == 2:
            return self.row2
        else:
            print("error")
            return [0, 0, 0]

    def getCol(self, num):
        if num == 0:
            col0 = [self.row0[0], self.row1[0], self.row2[0]]
            return col0
        if num == 1:
            col1 = [self.row0[1], self.row1[1], self.row2[1]]
            return col1
        if num == 2:
            col2 = [self.row0[2], self.row1[2], self.row2[2]]
            return col2
        else:
            print("error")
            return [0, 0, 0]

    def getDiag(self, num):
        if num == 1:
            diag1 = [self.row0[0], self.row1[1], self.row2[2]]
            return diag1
        if num == 2:
            diag2 = [self.row2[2], self.row1[1], self.row0[1]]
            return diag2

    def switchRow(self, num, row):
        if num == 0:
            self.row0 = row
            self.board = [self.row0, self.row1, self.row2]
            return self.board
        if num == 1:
            self.row0 = row
            self.board = [self.row0, self.row1, self.row2]
            return self.board
        if num == 2:
            self.row2 = row
            self.board = [self.row0, self.row1, self.row2]
            return self.board
        else:
            print("error")
            return self.board
