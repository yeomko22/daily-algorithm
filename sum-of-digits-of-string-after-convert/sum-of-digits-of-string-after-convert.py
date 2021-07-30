class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = ''.join([str(ord(c) - 96) for c in s])
        for i in range(k):
            digits = str(sum([int(x) for x in digits]))
        return digits