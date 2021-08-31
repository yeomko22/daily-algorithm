class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        answer = nums[0]
        while l < r:
            mid = (l + r) // 2
            answer = min(answer, min(min(nums[l], nums[r]), nums[mid]))
            if nums[l] < nums[mid]:
                if nums[r] < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r = mid - 1
        return answer