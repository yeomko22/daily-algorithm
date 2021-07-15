class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        while len(dp) < n + 1:
            tmp = []
            for i in range(len(dp)):
                tmp.append(dp[i] + 1)
            dp += tmp
        return dp[:n+1]