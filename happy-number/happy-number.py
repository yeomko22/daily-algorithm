class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            visited.add(n)
            tmp = 0
            for c in str(n):
                tmp += int(c) ** 2
            # print('n', n, 'tmp', tmp, 'visited', visited)
            if tmp == 1:
                return True
            if tmp in visited:
                break
            n = tmp
        return False