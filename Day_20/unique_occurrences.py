# =========================================================================
# Question: 1207. Unique Number of Occurrences
# Difficulty: Easy
# Topic: Hash Map & Hash Set
# -------------------------------------------------------------------------
# TIME COMPLEXITY: O(n) 
# - We iterate through the array once to build the frequency map.
# - Extracting values and creating a set also take linear time.
#
# SPACE COMPLEXITY: O(n)
# - We use a dictionary to store frequencies and a set for unique counts.
# - In the worst case, the size depends on the number of unique elements.
# =========================================================================

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # 1. Frequency Map: O(n) time, O(n) space
        char_arr = {}
        for i in arr:
            char_arr[i] = char_arr.get(i, 0) + 1
        
        # 2. Extract values: O(n) time, O(n) space
        count_list = char_arr.values()
        
        # 3. Set for uniqueness: O(n) time, O(n) space
        count_set = set(count_list)
        
        # 4. Comparison: O(1) time
        return len(count_list) == len(count_set)