class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        dp = []
        for i in range(len(self.matrix)):
            dp.append([0] * len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0:
                    dp[i][j] = matrix[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + matrix[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + matrix[i][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        cursum = self.dp[row2][col2]
        if col1 > 0 and row1 > 0:
            cursum -= self.dp[row2][col1-1]
            cursum -= self.dp[row1-1][col2]
            cursum += self.dp[row1-1][col1-1]
        elif col1 > 0:
            cursum -= self.dp[row2][col1-1]
        elif row1 > 0:
            cursum -= self.dp[row1-1][col2]
        return cursum        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)