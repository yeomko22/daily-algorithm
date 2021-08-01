class Solution:
    def reverseBits(self, n: int) -> int:
        binstr = str(bin(n))[2:]
        binstr = '0' * (32 - len(binstr)) + binstr
        binstr = binstr[::-1]
        return int(binstr, 2)