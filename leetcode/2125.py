class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for row in bank:
            cur = 0
            for col in row:
                if col == '1':
                    cur += 1
            if cur != 0:
                ans += (prev * cur)
                prev = cur
        return ans
        