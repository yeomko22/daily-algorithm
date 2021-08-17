class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        curmin = nums[k]
        answer = curmin
        while i > 0 or j < len(nums) -1:
            if i == 0:
                j += 1
                curmin = min(curmin, nums[j])
            elif j == len(nums)-1:
                i -= 1
                curmin = min(curmin, nums[i])
            elif nums[i-1] > nums[j+1]:
                i -= 1
                curmin = min(curmin, nums[i])
            else:
                j += 1
                curmin = min(curmin, nums[j])
            answer = max(answer, curmin * (j - i + 1))
        return answer