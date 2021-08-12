class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        dp = []
        for i in range(len(nums)):
            if i == 0:
                dp.append([nums[0], 0])
            elif i == 1:
                dp.append([nums[1], nums[0]])
            else:
                dp.append([0, 0])
        for i in range(2, len(nums)):
            dp[i][0] = max(dp[i-2][1], dp[i-1][1]) + nums[i]
            dp[i][1] = max(dp[i-2][0], dp[i-1][0])
        # print(dp)
        return max(dp[-1])