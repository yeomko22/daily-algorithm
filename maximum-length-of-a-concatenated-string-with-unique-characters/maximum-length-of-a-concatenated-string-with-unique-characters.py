class Solution:
    def maxLength(self, arr: List[str]) -> int:
        answer = 0
        arr = [x for x in arr if len(set(x)) == len(x)]
        def dfs(index, curstr):
            nonlocal answer
            if index > len(arr) -1:
                return
            for i in range(index, len(arr)):
                if set(arr[i]).intersection(set(curstr)):
                    continue
                answer = max(answer, len(curstr + arr[i]))
                dfs(i + 1, curstr + arr[i])
        dfs(0, '')
        return answer