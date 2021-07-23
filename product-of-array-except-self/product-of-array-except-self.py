class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        zeroindex = []
        mul = 1
        for i, num in enumerate(nums):
            if num == 0:
                zeroindex.append(i)
            else:
                mul *= num
        if len(zeroindex) >= 2:
            return answer
        if len(zeroindex) == 1:
            answer[zeroindex[0]] = mul
            return answer
        for i in range(len(nums)):
            answer[i] = mul // nums[i]
        return answer