"""
Question: 77. Combinations
Level: Medium
Topic: Backtracking with Pruning
Time Complexity: O(k * C(n, k)) - Where C(n, k) is the number of combinations.
Space Complexity: O(k) - Max depth of the recursion stack is k.
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def solve(start):
            # BASE CASE: If the current combination (path) reaches size k
            if len(path) == k:
                # Store a copy of the path
                result.append(path[:])
                return

            # OPTIMIZATION (PRUNING): 
            # We only start a loop if there are enough numbers left to complete the team.
            # Formula: n - (k - len(path)) + 2
            # This skips unnecessary recursive calls, making it super fast!
            for i in range(start, n - (k - len(path)) + 2):
                # 1. Action: Add the number to our current team
                path.append(i)
                
                # 2. Recurse: Move to the next number (i + 1)
                solve(i + 1)
                
                # 3. Backtrack: Remove the last number to try the next option
                path.pop()

        # Engine Start: Numbers start from 1
        solve(1)
        
        return result