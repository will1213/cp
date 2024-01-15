class Solution:
    def countBits(self, n: int) -> List[int]:
        # brute-force apporach
        # should use dp to be faster tho
        ans = []
        for i in range(n+1):
            s = bin(i)[2:]
            ans.append(s.count('1'))
        return ans