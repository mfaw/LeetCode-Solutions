class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]*(n+1) for n in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans