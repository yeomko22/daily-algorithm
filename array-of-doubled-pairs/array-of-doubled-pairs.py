class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        c = Counter(arr)
        cursum = 0
        q = deque(sorted(arr, key=lambda x: abs(x)))
        while q:
            if cursum == len(arr):
                break
            cur = q.popleft()
            if not c[cur]:
                continue
            if cur == 0:
                if c[cur] < 2:
                    return False
                else:
                    c[cur] -= 2
                    cursum += 2
            else:
                if not c[cur * 2]:
                    return False
                else:
                    c[cur * 2] -= 1
                    c[cur] -= 1
                    cursum += 2
        return True