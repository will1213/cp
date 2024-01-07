class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        res = 0
        for r in dimensions:
            d = math.sqrt(r[0] * r[0] + r[1] * r[1])
            if d == ans:
                res = max(res, r[0] * r[1])
            if d > ans:
                ans = d
                res = r[0] * r[1]
        return res