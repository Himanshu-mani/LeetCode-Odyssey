'''''
Question Number: 51
Name: N-Queens
Difficulty Level: Hard
Type: Backtracking / Constraint Satisfaction
Time Complexity: O(N!) - Exponential growth.
Space Complexity: O(N^2) for board storage and diagonal sets.
'''''
class Solution(object):
    def solveNQueens(self, n):
        res = []
        # Create an empty NxN board filled with dots
        board = [["."]* n for _ in range(n)]

        # Sets to keep track of columns and diagonals already occupied by queens
        cols = set()
        posDiag = set() # (row + col) is constant for anti-diagonals
        negDiag = set() # (row - col) is constant for main diagonals

        def backtrack(r):
            # If we placed queens in all rows, save the current board configuration
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                # If this position is under attack by another queen, skip it
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Place the queen and mark its column and diagonals as occupied
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Move to the next row to place the next queen
                backtrack(r + 1)

                # Remove the queen and clear the markers for other possibilities (Backtrack)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
        backtrack(0)
        return res