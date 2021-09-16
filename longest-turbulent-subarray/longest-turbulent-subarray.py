class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        answer = 1
        cur = 1
        # direction 1: up, 2: down, 3: same
        direction = 3
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                direction = 3
                cur = 1
            elif arr[i] > arr[i-1]:
                if direction == 2:
                    cur += 1
                else:
                    cur = 2
                direction = 1
            else:
                if direction == 1:
                    cur += 1
                else:
                    cur = 2
                direction = 2
            answer = max(answer, cur)
        return answer