class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        length = len(grid)
        yCount = {0:0, 1:0, 2:0}
        restCount = {0:0, 1:0, 2:0}
        half = length // 2
        for i in range(length):
            for j in range(length):
                if i < half:
                    if j == i or j == length-i-1:
                        yCount[grid[i][j]] += 1
                    else:
                        restCount[grid[i][j]] += 1
                else:
                    if j == half:
                        yCount[grid[i][j]] += 1
                    else:
                        restCount[grid[i][j]] += 1
        ans = math.inf
        for i in range(3):
            temp = 0
            for k, v in yCount.items():
                if k != i:
                    temp += v
            lo = math.inf
            for k, v in restCount.items():
                if k != i:
                    lo = min(lo, v)
            temp += lo
            temp += restCount[i]
            ans = min(ans, temp)
        return ans