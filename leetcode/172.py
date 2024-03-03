class Solution:
    def trailingZeroes(self, n: int) -> int:
        temp = 5
        count = 0
        while n // temp != 0:
            count += n // temp
            temp *= 5
        return count