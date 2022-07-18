class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        #presum of rows
        for i in range(m):
            for j in range(n-1):
                matrix[i][j+1] += matrix[i][j]
        result = 0
        # sum of pair of columns
        for x in range(n):
            for y in range(x,n):
                presum = {0: 1}
                s = 0
                for h in range(m):
                    s += matrix[h][y] - (matrix[h][x-1] if x > 0 else 0)
                    result += presum.get(s - target, 0)
                    presum[s] = presum.get(s, 0) + 1
        return result