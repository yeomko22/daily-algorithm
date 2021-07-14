class Solution:
    def customSortString(self, order: str, str: str) -> str:
        answer = ''
        d = {x:i for i, x in enumerate(order)}
        arr = []
        for c in str:
            if c in d:
                arr.append((c, d[c]))
            else:
                arr.append((c, 27))
        arr_sorted = sorted(arr, key=lambda x: x[1])
        for c, _ in arr_sorted:
            answer += c
        return answer