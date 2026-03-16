# Two Sum (LeetCode #1)
# Time Complexity: O(n) - We only scan the array once.
# Space Complexity: O(n) - In the worst case, we store all elements in the map.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a dictionary to store the numbers we have seen
        # Key: the number, Value: its index
        seen_numbers = {}

        for current_index, current_value in enumerate(nums):
            # Calculate what number we need to find
            needed_number = target - current_value

            # If the needed number is already in our dictionary, we found the pair
            if needed_number in seen_numbers:
                return [seen_numbers[needed_number], current_index]

            # If not found, add the current number and its index to the dictionary
            seen_numbers[current_value] = current_index

        # Return empty list if no solution is found
        return []