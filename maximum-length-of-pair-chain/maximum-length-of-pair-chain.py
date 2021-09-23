class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])
        cur = pairs[0]
        answer = 1
        for i in range(1, len(pairs)):
            if pairs[i][0] > cur[1]:
                answer += 1
                cur = pairs[i]
        return answer
