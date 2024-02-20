class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        visited = set()
        def helper(r, c):
            if 0 <= r < row and 0 <= c < col:
                position = f'{r}.{c}'
                if board[r][c] == "O" and position not in visited:
                    visited.add(position)
                    dirction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for y, x in dirction:
                        if not helper(r+y, c+x):
                            return False
                return True
            return False
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    visited = set()
                    if helper(i, j):
                        for p in visited:
                            position = p.split('.')
                            board[int(position[0])][int(position[1])] = "X"
        return