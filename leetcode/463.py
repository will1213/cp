class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ans = 0
        visited = set()
        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col:
                if grid[r][c] == 1:
                    position = f'{r}.{c}'
                    if position not in visited:
                        dirction = [[1,0], [-1,0], [0,1], [0,-1]]
                        ret = 4
                        visited.add(position)
                        for x, y in dirction:
                            ret -= dfs(r+x, c+y)
                        nonlocal ans
                        ans += ret
                    return 1
            return 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return ans
        return 