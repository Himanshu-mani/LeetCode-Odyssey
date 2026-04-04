# =========================================================================
# Question: 1748. Sum of Unique Elements
# Difficulty: Easy
# -------------------------------------------------------------------------
# TIME COMPLEXITY: O(n) 
# - We visit each number once to count it, and once more to sum it.
#
# SPACE COMPLEXITY: O(n) 
# - In the worst case, we store every element in the dictionary.
# =========================================================================

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Create a dictionary to store the count of each number
        count = {}

        # Step 2: Loop through the array and update frequencies
        for i in nums:
            # Using .get(i, 0) to avoid errors if the number is new
            count[i] = count.get(i, 0) + 1
            
        total_sum = 0

        # Step 3: Loop through the dictionary keys
        for i in count:
            # Only add the number if it appeared exactly once
            if count[i] == 1:
                total_sum += i
                
        return total_sum