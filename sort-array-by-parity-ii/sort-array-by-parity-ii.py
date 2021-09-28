class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        even_index = 0
        odd_index = 1
        for num in nums:
            if num % 2:
                answer[odd_index] = num
                odd_index += 2
            else:
                answer[even_index] = num
                even_index += 2
        return answer