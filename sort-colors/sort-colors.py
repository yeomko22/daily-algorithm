class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        color = 0
        color_cnt = c[color]
        for i in range(len(nums)):
            while True:
                if not color_cnt:
                    color += 1
                    color_cnt = c[color]
                    continue
                nums[i] = color
                color_cnt -= 1
                break
        return nums
