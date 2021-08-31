class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def neighborcnt(row, col):
            moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            neighbors = 0
            for move in moves:
                newrow = row + move[0]
                newcol = col + move[1]
                if newrow < 0 or newcol < 0 or newrow > len(board) -1 or newcol > len(board[0]) -1:
                    continue
                if board[newrow][newcol]:
                    neighbors += 1
            return neighbors
        
        neighborboard = []
        for i in range(len(board)):
            neighborboard.append([0] * len(board[0]))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighborboard[i][j] = neighborcnt(i, j)
                
        # for i in range(len(neighborboard)):
        #     print(neighborboard[i])
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if neighborboard[i][j] < 2 or neighborboard[i][j] > 3:
                    board[i][j] = 0
                elif neighborboard[i][j] == 3:
                    board[i][j] = 1