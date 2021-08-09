class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        answer = 1
        for v in s:
            if v - 1 in s:
                continue
            cur = copy.deepcopy(v)
            cnt = 1
            while True:
                if cur + 1 in s:
                    cnt += 1
                    cur += 1
                else:
                    break
            answer = max(answer, cnt)
        return answer