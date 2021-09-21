class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur = 0
                continue
            if nums[i] == 1:
                cur += 1
                answer = max(answer, cur)
        return answer