class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sortedarr = []
        n = len(matrix)
        indexes = [0] * n
        while indexes != [len(matrix)] * n:
            minval = float('inf')
            minindex = -1
            for i in range(n):
                if indexes[i] == n:
                    continue
                curval = matrix[i][indexes[i]]
                if curval < minval:
                    minval = curval
                    minindex = i
            sortedarr.append(minval)
            indexes[minindex] += 1
            # print(sortedarr, minval, minindex)     
        return sortedarr[k - 1]