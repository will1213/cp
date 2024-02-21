class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row = len(grid1)
        col = len(grid1[0])
        visited = set()
        dp = [[1] * col for _ in range(row)]
        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col:
                position = f"{r}.{c}"
                if grid2[r][c] == 1:
                    if grid1[r][c] == 0:
                        return False
                    if position in visited:
                        return dp[r][c]
                    if position not in visited:
                        direction = [[1,0], [-1,0], [0,1], [0,-1]]
                        visited.add(position)
                        for x, y in direction:
                            if not dfs(r+x, c+y):
                                dp[r][c] = 0
                                return False
            return True 
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and f"{i}.{j}" not in visited:
                    if dfs(i, j):
                        ans += 1
        return ans
