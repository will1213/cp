class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0
        myGrid = [[math.inf] * col for _ in range(row)]
        for i in range(row):
            curSum = 0
            for j in range(col):
                curSum += grid[i][j]
                temp = curSum
                if i > 0:
                    temp += myGrid[i-1][j]
                myGrid[i][j] = temp
                if temp > k:
                    break
                ans += 1
        return ans