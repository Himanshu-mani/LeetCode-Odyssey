# Type: Combination Mapping Pattern
# Difficulty: Medium
# Time Complexity: O(4^N) where N is digits length
# Space Complexity: O(N)

class Solution:
    def letterCombinations(self, digits):
        if not digits: return []
        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
                   "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        def solve(index, path):
            # Base Case: Processed all digits
            if index == len(digits):
                res.append(path)
                return
            
            # Get letters for the current digit and try each one
            for char in mapping[digits[index]]:
                solve(index + 1, path + char) # Implicit backtracking with strings

        solve(0, "")
        return res