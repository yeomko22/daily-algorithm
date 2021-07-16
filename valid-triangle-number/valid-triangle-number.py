class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for i in range(2, len(nums)):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] <= nums[i]:
                    l += 1
                else:
                    answer += r - l
                    r -= 1
        return answer