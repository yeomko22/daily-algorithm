class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        # print(nums)
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                triplet = (nums[i], nums[j], nums[k])
                cursum = sum(triplet)
                if cursum == 0:
                    answer.add(triplet)
                if cursum < 0:
                    j += 1
                else:
                    k -= 1
        answer = [list(x) for x in answer]
        return answer