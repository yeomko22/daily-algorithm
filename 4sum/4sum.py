class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        nums.sort()
        for i in range(3, len(nums)):
            for j in range(2, i):
                l = 0
                r = j - 1
                while l < r:
                    cursum = nums[i] + nums[j] + nums[l] + nums[r]
                    if cursum == target:
                        answer.add((nums[l], nums[r], nums[j], nums[i]))
                        l += 1
                    elif cursum > target:
                        r -= 1
                    else:
                        l += 1
        return list(answer)