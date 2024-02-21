class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0:
            return 0
        temp = 1
        while temp <= left:
            temp = temp << 1
        temp = min(temp,right)
        while temp > left:
            temp = temp & (temp-1)
        return left & temp