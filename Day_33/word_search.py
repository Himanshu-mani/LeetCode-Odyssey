'''''
Question Number: 79
Name: Word Search
Difficulty Level: Medium
Type: Backtracking / 2D Grid DFS
Time Complexity: O(N * M * 3^L) where N*M is board size and L is word length.
Space Complexity: O(L) for recursion stack.
'''''
class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(r, c, index):
            # If we matched all characters in the word, return True
            if index == len(word):
                return True

            # Check if we are out of the board or if the character doesn't match
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]):
                return False
            
            # Save the current character and mark this cell as visited using "#"
            temp = board[r][c]
            board[r][c] = "#"

            # Search in all 4 directions: Down, Up, Right, Left
            found = (backtrack(r+1, c, index+1) or 
                    backtrack(r-1, c, index+1) or 
                    backtrack(r, c+1, index+1) or 
                    backtrack(r, c-1, index+1))

            # After searching, put the original character back (Backtrack)
            board[r][c] = temp
            return found

        # Start the search from every cell in the board
        for r in range(rows):
            for c in range(cols):
                # Only start backtracking if the first letter matches
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False