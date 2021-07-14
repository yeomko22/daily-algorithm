class Solution:
    def countTriples(self, n: int) -> int:
        squares = [x*x for x in range(1, n + 1)]
        s = set(squares)
        answer = 0
        for i in range(len(squares)):
            for j in range(i + 1, len(squares)):
                # print(squares[i], squares[j], squares[i] + squares[j])
                if squares[i] + squares[j] in s:
                    answer += 2
        return answer