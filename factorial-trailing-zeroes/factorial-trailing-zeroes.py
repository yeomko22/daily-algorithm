class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer = 0
        for i in range(1, n+1):
            tmp = i
            while True:
                if tmp % 5 == 0:
                    answer += 1
                    tmp = tmp // 5
                else:
                    break
        return answer