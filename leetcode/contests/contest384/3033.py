class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        ans = [[0] * c for _ in range(r)]
        for i in range(c):
            rowToChange = []
            myMax = matrix[0][i]
            for j in range(r):
                if matrix[j][i] == -1:
                    rowToChange.append(j)
                else:
                    ans[j][i] = matrix[j][i]
                myMax = max(myMax, matrix[j][i])
            for row in rowToChange:
                ans[row][i] = myMax
        return ans
                    