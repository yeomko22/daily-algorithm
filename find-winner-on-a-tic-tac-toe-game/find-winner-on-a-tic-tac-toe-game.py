class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[" " for x in range(3)] for y in range(3)]
        def checkwin(row, col):
            target = board[row][col]
            if board[row][0] == board[row][1] == board[row][2] == target:
                return True
            if board[0][col] == board[1][col] == board[2][col] == target:
                return True
            if board[0][0] == board[1][1] == board[2][2] == target:
                return True
            if board[2][0] == board[1][1] == board[0][2] == target:
                return True
            return False
        playerA = True
        for move in moves:
            row, col = move
            if playerA:
                board[row][col] = "X"
                playerA = False
                if checkwin(row, col):
                    return "A"
            else:
                board[row][col] = "O"
                playerA = True
                if checkwin(row, col):
                    return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"