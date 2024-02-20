class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = 0
        visited = set()

        def helper(r, c, count):
            if 0 <= r < row and 0 <= c < col:
                location = f'{r}.{c}'
                if location not in visited:
                    if grid[r][c] == 1:
                        ret = count
                        visited.add(location)
                        dirction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                        for x, y in dirction:
                            ret += helper(r+x, c+y, count)
                        ret += 1
                        return ret
            return 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i + (j * 0.1)) not in visited:
                    ans = max(helper(i, j, 0), ans)
                else:
                    visited.add(f'{i}.{j}')
        return ans