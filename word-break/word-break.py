class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        answer = False
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for word in wordDict:
                if i < len(word):
                    continue
                if s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True
        return dp[-1]
