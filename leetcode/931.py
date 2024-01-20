class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        l = len(matrix)
        def helper(row, last):
            if row < l:
                temp = []
                myMin = deque()
                myMin.append(last[0])
                myMin.append(last[1])
                temp.append(min(myMin)+matrix[row][0])
                for i in range(1, l-1):
                    myMin.append(last[i+1])
                    temp.append(min(myMin)+matrix[row][i])
                    myMin.popleft()
                temp.append(min(last[-2], last[-1])+matrix[row][-1])
                return helper(row+1, temp)
            return last
        return min(helper(1, matrix[0]))