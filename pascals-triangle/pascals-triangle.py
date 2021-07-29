class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        dp = [1]
        for i in range(1, numRows):
            newdp = [0] * (len(dp) + 1)
            newdp[0] = dp[0]
            newdp[-1] = dp[-1]
            for j in range(1, len(newdp)-1):
                newdp[j] = dp[j-1] + dp[j]
            # print('dp', dp, 'newdp', newdp)
            answer.append(newdp)
            dp = newdp
        return answer