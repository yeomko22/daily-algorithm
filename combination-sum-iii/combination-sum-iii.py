class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        def dfs(curarr, num):
            cursum = sum(curarr)
            # print(curarr, num)
            if len(curarr) == k:
                if cursum == n:
                    answer.append(curarr)
                return
            for i in range(num + 1, 10):
                if cursum + i <= n:
                    dfs(curarr + [i], i)
        dfs([], 0)
        return answer