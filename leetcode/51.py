class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def helper(arr, row, usedCol):
            if row < n:
                for i in range(n):
                    if i not in usedCol:
                        nextIndex = False
                        for r, index in enumerate(arr):
                            if (row-r) / (i-index) in [1.0, -1.0]:
                                nextIndex = True
                                break
                        if nextIndex:
                            continue
                        else:
                            temp = usedCol.copy()
                            temp.add(i)
                            helper(arr+[i], row+1, temp)
            else:
                a = []
                for i in range(n):
                    temp = '.' * arr[i]
                    temp += 'Q'
                    temp += '.' * (n - arr[i]-1)
                    a.append(temp)
                ans.append(a)
            return
        ans = []
        for i in range(n):
            used = set()
            used.add(i)
            helper([i], 1, used)
        return ans

                
