class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [x for x in c if c[x] == 1]