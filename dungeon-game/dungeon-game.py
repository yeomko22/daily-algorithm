class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        dp[-1][-1] = dungeon[-1][-1] * -1 + 1 if dungeon[-1][-1] < 0 else 1
        
        def print_dp():
            for i in range(len(dp)):
                print(dp[i])
            print('')
                
        for i in range(1, m):
            index = m - 1 - i
            dp[index][-1] = max(dp[index + 1][-1] - dungeon[index][-1], 1)
        
        for i in range(1, n):
            index = n - 1 - i
            dp[-1][index] = max(dp[-1][index + 1] - dungeon[-1][index], 1)
                
        for i in range(m-1):
            for j in range(n-1):
                index_m = m - 2 - i
                index_n = n - 2 - j
                dp[index_m][index_n] = max(min(dp[index_m+1][index_n], dp[index_m][index_n+1]) - dungeon[index_m][index_n], 1)
        # print_dp()
        return dp[0][0]
