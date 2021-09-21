class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        a = [True] * (n + 1)
        a[0] = False
        a[1] = False
        answer = 0
        for i in range(2,n):
            if a[i]:
                answer += 1
                for j in range(2*i, n+1, i):
                    a[j] = False
        return answer
