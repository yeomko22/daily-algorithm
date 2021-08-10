class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer = -1
        q = [(0, 0)]
        visited = set()
        while q:
            cur, level = q.pop(0)
            if cur in visited or cur > amount:
                continue
            visited.add(cur)
            # print('cur', cur, 'level', level, 'visited', visited)
            if cur == amount:
                answer = level
                break
            for coin in coins:
                if cur + coin not in visited:
                    q.append((cur+coin, level+1))
        return answer
        