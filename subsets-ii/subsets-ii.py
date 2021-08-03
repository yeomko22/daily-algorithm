class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        def dfs(subset, index):
            if subset in answer:
                return
            answer.append(subset)
            for i in range(index, len(nums)):
                dfs(subset + [nums[i]], i + 1)
        dfs([], 0)
        return answer