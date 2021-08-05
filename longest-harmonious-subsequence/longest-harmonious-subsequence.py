class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        answer = 0
        keys = sorted(c.keys())
        for key in keys:
            if key + 1 in c:
                answer = max(c[key] + c[key + 1], answer)
        return answer