# =========================================================================
# Question: 380. Insert Delete GetRandom O(1)
# Difficulty: Medium
# Topic: Hash Map & Array (Hybrid Data Structure)
# -------------------------------------------------------------------------
# Time Complexity:
#   - Insert: O(1)
#   - Remove: O(1)
#   - GetRandom: O(1)
# Space Complexity: O(n) - where n is the number of elements stored.
# =========================================================================

import random

class RandomizedSet(object):

    def __init__(self):
        """
        Constructor: Initialize two containers.
        - data_list: To store values (helps in O(1) random access).
        - index_map: To store {Value: Index} (helps in O(1) lookup).
        """
        self.data_list = []
        self.index_map = {}

    def insert(self, val):
        """
        Goal: Add a value if it's not already present.
        """
        # 1. If value already exists, we don't add it.
        if val in self.index_map:
            return False
        
        # 2. Store the index where this value will be placed in the list.
        self.index_map[val] = len(self.data_list)
        
        # 3. Add the value to the end of the list.
        self.data_list.append(val)
        return True

    def remove(self, val):
        """
        Goal: Remove a value in O(1) without shifting the whole array.
        """
        # 1. If value doesn't exist, we can't remove it.
        if val not in self.index_map:
            return False
        
        # 2. Get the index of the element we want to remove.
        idx_to_remove = self.index_map[val]
        
        # 3. Find the last element currently in the list.
        last_element = self.data_list[-1]
        
        # 4. THE SWAP TRICK:
        # Put the last element in the spot of the element we want to delete.
        self.data_list[idx_to_remove] = last_element
        
        # 5. Update the Map with the last element's new position.
        self.index_map[last_element] = idx_to_remove
        
        # 6. CLEAN UP:
        # Remove the last element from the list (O(1) pop).
        self.data_list.pop()
        # Delete the target value from the map.
        del self.index_map[val]
        
        return True

    def getRandom(self):
        """
        Goal: Pick any element from the list with equal probability.
        """
        # Python's random.choice works in O(1) on lists using indexing.
        return random.choice(self.data_list)

# Execution logic:
# obj = RandomizedSet()
# print(obj.insert(1))   # Returns True
# print(obj.remove(2))   # Returns False
# print(obj.getRandom()) # Returns 1