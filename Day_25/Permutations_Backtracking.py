"""
Question: 46. Permutations
Level: Medium
Topic: Backtracking / Recursion
Time Complexity: O(n * n!) - n! permutations, each taking O(n) to copy.
Space Complexity: O(n) - Maximum depth of the recursion stack (no extra visited array).
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        # Professional standard: Helper function for in-place swapping
        def backtrack(index):
            # BASE CASE: If we have filled all the "chairs" (index reaches end)
            if index == len(nums):
                # We append a copy of current nums because lists are mutable
                result.append(nums[:])
                return
            
            # Iterate through all available elements for the current chair
            for i in range(index, len(nums)):
                # 1. SWAP: Put the chosen element 'i' into the current chair 'index'
                nums[index], nums[i] = nums[i], nums[index]
                
                # 2. RECURSE: Move to fill the next chair
                backtrack(index + 1)
                
                # 3. BACKTRACK (U-Turn): Swap back to restore original array
                # This is crucial so the next iteration of the loop works correctly
                nums[index], nums[i] = nums[i], nums[index]

        # Engine Start: Begin with the first chair (index 0)
        backtrack(0)
        
        return result