class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if f != d:
            temp = (e - c) / (f-d)
            if temp in [-1, 1]:
                if b!=d:
                    if temp == ((a-c) / (b-d)):
                        if a in range(min(c,e), max(c,e)+1) and b in range(min(d,f), max(d,f)):
                            return 2
                return 1
        if a == e:
            if e != c:
                return 1
            elif d not in range(min(b,f), max(b,f)+1):
                return 1
            return 2
        if f == b:
            if f != d:
                return 1
            elif c not in range(min(a,e), max(a,e)+1):
                return 1
            return 2
        else:
            return 2