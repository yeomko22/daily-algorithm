class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if not rows:
            return mat
        cols = len(mat[0])
        answer = []
        q = []
        for i in range(rows):
            answer.append([float('inf')] * cols)
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    answer[i][j] = 0
                    q.append((i, j))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            currow, curcol = q.pop(0)
            for i in range(len(dirs)):
                newrow = currow + dirs[i][0]
                newcol = curcol + dirs[i][1]
                if newrow >= 0 and newcol >= 0 and newrow < rows and newcol < cols:
                    if answer[newrow][newcol] > answer[currow][curcol] + 1:
                        answer[newrow][newcol] = answer[currow][curcol] + 1
                        q.append((newrow, newcol))
        return answer