class Solution:
    def numDecodings(self, s: str) -> int:
        answer = 0
        dp = [0] * (len(s))
        if s[0] == '0':
            return answer
        dp[0] = 1
        if len(s) > 1:
            if s[1] != '0':
                dp[1] += 1
            if int(s[:2]) < 27 and int(s[:2]) >= 10:
                dp[1] += 1
        for i in range(2, len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if s[i-1] != '0' and int(s[i-1:i+1]) < 27:
                dp[i] += dp[i-2]
        return dp[-1]