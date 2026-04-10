# Type: Permutation Pattern
# Difficulty: Medium
# Time Complexity: O(N * N!)
# Space Complexity: O(N) for recursion depth

class Solution:
    def permute(self, nums):
        res = []
        used = [False] * len(nums) # Track which numbers are picked

        def backtrack(path):
            # Base Case: All numbers are in the path
            if len(path) == len(nums):
                res.append(path[:]) # Store a copy of current path
                return
            
            for i in range(len(nums)):
                if not used[i]: # If number is not yet picked
                    used[i] = True # Action: Mark as used
                    path.append(nums[i])
                    backtrack(path) # Recurse: Go to next level
                    path.pop() # Backtrack: Remove and try next
                    used[i] = False
        
        backtrack([])
        return res