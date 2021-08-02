class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        d = {0: 0}
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        island_id = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or grid[i][j] > 1:
                    continue
                q = [(i, j)]
                cnt = 0
                while q:
                    row, col = q.pop(0)
                    if grid[row][col] > 1:
                        continue
                    grid[row][col] = island_id
                    cnt += 1
                    for move in moves:
                        newrow = row + move[0]
                        newcol = col + move[1]
                        if newrow < 0 or newrow > len(grid) - 1:
                            continue
                        if newcol < 0 or newcol > len(grid[0]) - 1:
                            continue
                        if grid[newrow][newcol] != 1:
                            continue
                        q.append((newrow, newcol))
                d[island_id] = cnt
                island_id += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    continue
                curcnt = 1
                neighbors = set()
                for move in moves:
                    newrow = i + move[0]
                    newcol = j + move[1]
                    if newrow < 0 or newrow > len(grid) - 1:
                        continue
                    if newcol < 0 or newcol > len(grid[0]) - 1:
                        continue
                    if grid[newrow][newcol] == 0:
                        continue
                    neighbors.add(grid[newrow][newcol])
                for neighbor in neighbors:
                    curcnt += d[neighbor]
                answer = max(answer, curcnt)
        if answer == 0:
            answer = max(d.values())
        # print(d)
        # for i in range(len(grid)):
        #     print(grid[i])
        return answer