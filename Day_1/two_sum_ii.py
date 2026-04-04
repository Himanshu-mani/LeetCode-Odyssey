# Problem: Two Sum II - Input Array Is Sorted (LeetCode 167)
# Approach: Two Pointers (Optimal for Sorted Arrays)
# Time Complexity: O(n) - Single pass through the array
# Space Complexity: O(1) - Constant space usage

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            # Case 1: Target found
            if current_sum == target:
                # Return 1-based indices as per LeetCode requirement
                return [left + 1, right + 1]
            
            # Case 2: Sum is too small, move left pointer forward to increase sum
            elif current_sum < target:
                left += 1
                
            # Case 3: Sum is too large, move right pointer backward to decrease sum
            else:
                right -= 1
        
        # Note: Problem guarantees exactly one solution exists.
        return []



        