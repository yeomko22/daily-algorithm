class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt_one = 0
        flips = 0
        for c in s:
            if c == '1':
                cnt_one += 1
            else:
                flips += 1
            flips = min(flips, cnt_one)
        return flips
