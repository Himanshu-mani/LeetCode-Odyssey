"""
Question: 78. Subsets
Level: Medium
Topic: Backtracking / Recursion
Time Complexity: O(2^n * n) - 2^n subsets, each taking O(n) to copy.
Space Complexity: O(n) - Maximum depth of the recursion stack.
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        # Helper function for backtracking logic
        def backtrack(index, path):
            # Base Case: If we have considered all elements
            if index == len(nums):
                # Append a copy of the current path to the result
                result.append(path[:])
                return

            # OPTION 1: "Pick" the current element
            path.append(nums[index])
            # Move to the next index with the element in our path
            backtrack(index + 1, path)
            
            # BACKTRACK: Remove the element to explore the "Don't Pick" option
            path.pop()
            
            # OPTION 2: "Don't Pick" the current element
            # Move to the next index without adding the element
            backtrack(index + 1, path)

        # Start the recursion from index 0 with an empty path
        backtrack(0, [])
        
        return result