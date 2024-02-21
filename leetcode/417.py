class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pac = [[-1] * col for _ in range(row)]
        atl = [[-1] * col for _ in range(row)]
        ans = []
        visited = set()
        for i in range(row):
            pac[i][0] = 1
            atl[i][col-1] = 1
        for i in range(col):
            pac[0][i] = 1
            atl[row-1][i] = 1
        def helper(r, c, prev, ocean):
            if 0 <= r < row and 0 <= c < col:
                position = f'{r}.{c}'
                if heights[r][c] <= prev and position not in visited:
                    if ocean:
                        if pac[r][c] == 1:
                            return True
                        elif pac[r][c] == 0:
                            return False
                    else:
                        if atl[r][c] == 1:
                            return True
                        elif atl[r][c] == 0:
                            return False
                    dirction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                    visited.add(f'{r}.{c}')
                    for x, y in dirction:
                        if helper(r+x, c+y, heights[r][c], ocean):
                            if ocean:
                                pac[r][c] = 1
                            else:
                                atl[r][c] = 1
                            return True
                        else:
                            if not visited:
                                if ocean:
                                    pac[r][c] = 0
                                else:
                                    atl[r][c] = 0
            return False
        for i in range(row):
            for j in range(col):
                visited = set()
                temp = helper(i, j, heights[i][j], 0)
                visited = set()
                temp2 = helper(i, j, heights[i][j], 1)
                if temp and temp2:
                    ans.append([i,j])
        return ans
