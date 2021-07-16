class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = 0
        nums.sort()
        # print(nums)
        diff = float('inf')
        for i in range(2, len(nums)):
            l = 0
            r = i - 1
            while l < r:
                cursum = nums[i] + nums[l] + nums[r]
                curdiff = target - cursum
                if abs(curdiff) < diff:
                    answer = cursum
                    diff = abs(curdiff)
                # print('l', l, 'r', r, 'diff', diff, 'curdiff', curdiff, 'cursum', cursum, 'answer', answer)
                if curdiff > 0:
                    l += 1
                else:
                    r -= 1
        return answer
        