class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnts = sorted(Counter(arr).values(), reverse=True)
        answer, cursum = (0, 0)
        for i in range(len(cnts)):
            cursum += cnts[i]
            answer += 1
            if cursum >= len(arr) // 2:
                break
        return answer