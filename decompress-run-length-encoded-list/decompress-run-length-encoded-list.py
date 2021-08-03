class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums) // 2):
            freq = nums[i*2]
            val = nums[i*2 + 1]
            answer += [val] * freq
        return answer