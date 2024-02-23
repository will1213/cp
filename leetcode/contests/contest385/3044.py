class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        
        row = len(mat)
        col = len(mat[0])
        
        myDict = defaultdict(int)
        numberDict = defaultdict(int)
        def isPrime(n):
            if n % 2 == 0:
                return False
            if n in numberDict:
                return numberDict[n]
            for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                    numberDict[n] = 0
                    return False
            numberDict[n] = 1
            return True

        def helper(r, c, dirc, cur):
            if 0 <= r < row and 0 <= c < col:
                cur = cur*10 + mat[r][c]
                if cur > 10 and isPrime(cur):
                    myDict[cur] += 1
                helper(r+dirc[0], c+dirc[1], dirc, cur)
            return

        dirction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for i in range(row):
            for j in range(col):
                for d in dirction:
                    helper(i, j, d, 0)
        if myDict:
            ans = 0
            myMax = max(myDict.values())
            for k, v in myDict.items():
                if v == myMax:
                    ans = max(ans, k)
            return ans
        return -1
                
                