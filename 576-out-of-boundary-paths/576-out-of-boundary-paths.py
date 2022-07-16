class Solution:
    m = None
    n = None
    lookup = None
    def solve(self, r, c, moves):
        if r<0 or c<0 or c>=self.n or r>= self.m:
            return 1
        if moves == 0:
            return 0
        if self.lookup[r][c][moves-1]!=-1:
            return self.lookup[r][c][moves-1]
        answer = self.solve(r+1, c, moves-1) + self.solve(r-1, c, moves-1) + self.solve(r, c+1, moves-1) + self.solve(r, c-1, moves-1)
        self.lookup[r][c][moves-1] = answer
        return answer
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = pow(10,9) + 7
        self.m = m
        self.n = n
        self.lookup = [[[-1 for m in range(maxMove)]for j in range(n)] for i in range(m)]
        return self.solve(startRow,startColumn,maxMove) % mod
        
        