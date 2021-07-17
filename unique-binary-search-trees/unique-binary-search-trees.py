class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for k in range(1, i + 1):
                dp[i] += dp[i-k] * dp[k-1]
                # print('dp', dp, 'i-k', i-k, 'dp[i-k]', dp[i-k], 'k-1', k-1, 'dp[k-1]', dp[k-1])
        return dp[n]