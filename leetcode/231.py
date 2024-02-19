class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        setBit = False
        myBin = f'{n:b}'
        for i in range(len(myBin)):
            if myBin[i] == '1':
                if setBit:
                    return False
                else:
                    setBit = True
        return True