# Type: Valid State Generation
# Difficulty: Medium
# Time Complexity: O(4^N / sqrt(N)) - Catalan Number
# Space Complexity: O(N)

class Solution:
    def generateParenthesis(self, n):
        res = []

        def solve(open_c, close_c, path):
            # Base Case: Path length is 2*n
            if len(path) == 2 * n:
                res.append(path)
                return
            
            # Decision 1: Add opening bracket if limit not reached
            if open_c < n:
                solve(open_c + 1, close_c, path + "(")
            
            # Decision 2: Add closing bracket only if it's safe (close < open)
            if close_c < open_c:
                solve(open_c, close_c + 1, path + ")")

        solve(0, 0, "")
        return res