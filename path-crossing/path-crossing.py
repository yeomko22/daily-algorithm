class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur = (0, 0)
        visited = set([cur])
        d = {'N': (1, 0), 'S': (-1, 0), 'E': (0, 1), 'W': (0, -1)}
        for c in path:
            moved = (cur[0] + d[c][0], cur[1] + d[c][1])
            if moved in visited:
                return True
            visited.add(moved)
            cur = moved
            # print(visited)
        return False