class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        answer = float('inf')
        nums.sort()
        for i in range(len(nums) -k + 1):
            answer = min(answer, nums[i + k - 1] - nums[i])
        return answer