class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        lines = set()
        overlap = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]:
                    continue
                square = [(i, j, i, j+1), (i, j, i+1, j), (i, j+1, i+1, j+1), (i+1, j, i+1, j+1)]
                for line in square:
                    if line in lines:
                        overlap.add(line)
                    lines.add(line)
        return len(lines) - len(overlap)