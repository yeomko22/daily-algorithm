class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = False
        i = 0
        prev = 10001
        for j in range(len(nums)):
            if nums[j] == prev:
                if not flag:
                    nums[i] = nums[j]
                    i += 1
                    flag = True
            else:
                prev = nums[j]
                flag = False
                nums[i] = nums[j]
                i += 1
        return i
                