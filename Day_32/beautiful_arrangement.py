# Type: Conditional Permutation
# Difficulty: Medium
# Time Complexity: O(Number of Valid Arrangements)
# Space Complexity: O(N)

class Solution:
    def countArrangement(self, n):
        self.count = 0
        used = [False] * (n + 1)

        def solve(pos):
            # Base Case: All positions filled
            if pos > n:
                self.count += 1
                return

            for val in range(1, n + 1):
                # Beautiful Check: Rule must be satisfied to proceed
                if not used[val] and (val % pos == 0 or pos % val == 0):
                    used[val] = True # Lock value
                    solve(pos + 1)
                    used[val] = False # Unlock value
        
        solve(1)
        return self.count