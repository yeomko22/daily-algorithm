class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        answer = False
        if sum(nums) % k:
            return answer
        target = sum(nums) // k
        for num in nums:
            if num > target:
                return answer
            
        def recursion(cnt, cur, nums):
            nonlocal answer
            if answer:
                return
            if cnt == k:
                answer = True
                return
            cursum = sum(cur)
            for i, num in enumerate(nums):
                if num + cursum < target:
                    recursion(cnt, cur + [nums[i]], nums[:i] + nums[i+1:])
                elif num + cursum == target:
                    recursion(cnt + 1, [], nums[:i] + nums[i+1:])
        recursion(0, [], sorted(nums, reverse=True))
        return answer