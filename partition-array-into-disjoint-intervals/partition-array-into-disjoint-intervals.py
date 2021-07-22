class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        l_dp = [-1] * len(nums)
        r_dp = [-1] * len(nums)
        l_max = -1
        r_min = 1000001
        for i in range(len(nums)):
            if nums[i] > l_max:
                l_max = nums[i]
            l_dp[i] = l_max
            j = len(nums) -1 -i
            if nums[j] < r_min:
                r_min = nums[j]
            r_dp[j] = r_min
        answer = 0
        for i in range(len(nums) - 1):
            if l_dp[i] <= r_dp[i+1]:
                answer = i + 1
                break
        return answer