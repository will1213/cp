class Solution:
    def numSquares(self, n: int) -> int:
        myDict = dict()
        def helper(n):
            if n == 0:
                return 0
            if n < 0:
                return math.inf
            if n in myDict:
                return myDict[n]
            start = math.floor(sqrt(n))
            temp = n
            for i in range(start, 0, -1):
                temp = min(temp, helper(n-i*i)+1)

            myDict[n] = temp
            return temp
        helper(n)            
        return myDict[n]