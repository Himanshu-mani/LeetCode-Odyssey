# Day 11: Contains Duplicate (LeetCode #217)
# Time Complexity: O(n) - We scan the array once.
# Space Complexity: O(n) - We store unique elements in a set.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create an empty set to store numbers we have seen
        seen_numbers = set()

        for n in nums:
            # If the number is already in the set, it's a duplicate
            if n in seen_numbers:
                return True
            
            # If not seen before, add it to the set
            seen_numbers.add(n)

        # If loop finishes without finding duplicates, return False
        return False