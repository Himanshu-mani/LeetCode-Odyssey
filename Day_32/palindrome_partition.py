# Type: String Partitioning Pattern
# Difficulty: Medium
# Time Complexity: O(N * 2^N)
# Space Complexity: O(N)

class Solution:
    def partition(self, s):
        res = []

        def is_pal(sub): # Check if segment is a palindrome
            return sub == sub[::-1]

        def backtrack(start, path):
            # Base Case: Reached the end of string
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start, len(s)):
                segment = s[start : end+1]
                # Guard Check: Only proceed if current segment is palindrome
                if is_pal(segment):
                    path.append(segment)
                    backtrack(end + 1, path)
                    path.pop() # Backtrack to try different cut

        backtrack(0, [])
        return res