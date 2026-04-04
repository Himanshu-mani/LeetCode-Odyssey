# =========================================================================
# Question: 36. Valid Sudoku
# Difficulty: Medium
# -------------------------------------------------------------------------
# TIME COMPLEXITY: O(1) 
# - Since the board size is fixed at 9x9, the operations are constant.
#
# SPACE COMPLEXITY: O(1) 
# - We store a fixed amount of data in the sets (max 81 entries).
# =========================================================================

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Step 1: Create 3 lists of sets to track Rows, Columns, and 3x3 Boxes
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Step 2: Loop through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # If the cell is empty (.), skip it
                if val == ".":
                    continue

                # Step 3: Calculate the Box ID for the current (r, c)
                # This divides the 9x9 board into nine 3x3 sub-grids (0 to 8)
                idx = (r // 3) * 3 + (c // 3)

                # Step 4: Triple Validation
                # Check if the number already exists in current Row, Column, or Box
                if (val in rows[r] or 
                    val in columns[c] or 
                    val in boxes[idx]):
                    return False # Conflict found! Sudoku is invalid.

                # Step 5: If no conflict, add the number to all 3 records
                rows[r].add(val)
                columns[c].add(val)
                boxes[idx].add(val)

        # If we check all cells without a conflict, return True
        return True