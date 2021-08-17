class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            cursum = nums[i]
            sums.append(cursum)
            for j in range(i+1, len(nums)):
                cursum += nums[j]
                sums.append(cursum)
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)
