class Solution:   
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = max(area, self.visit(grid, i, j))
                    print(area)
        return area
    
    def visit(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return 0
        if grid[row][col] == 0:
            return 0
        grid[row][col] = 0 # visited
        return 1 + self.visit(grid, row, col - 1) + self.visit(grid, row, col + 1) + self.visit(grid, row - 1, col) + self.visit(grid, row + 1, col)  
        
        