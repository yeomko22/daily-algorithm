class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums)):
            if not dp[i]:
                continue
            for j in range(nums[i]):
                if i+j+1 > len(nums) - 1:
                    return True
                dp[i+j+1] = True
                # print(dp)
        return dp[-1]
        