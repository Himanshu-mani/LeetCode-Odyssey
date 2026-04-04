# Problem: Minimum Size Subarray Sum
# Difficulty: Medium
# Time Complexity: O(n) - Each element is visited at most twice (by left and right pointers)
# Space Complexity: O(1) - Constant space used for pointers and variables

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        current_sum = 0
        min_length = float('inf')  # Using infinity to track the minimum value effectively
        
        # 'i' acts as the 'right' pointer expanding the window
        for i in range(len(nums)):
            current_sum += nums[i]
            
            # Shrink the window as long as the condition (current_sum >= target) is met
            while current_sum >= target:
                # Update the minimum length before shrinking the window
                min_length = min(min_length, i - left + 1)
                
                # Subtract the leftmost element and move the left pointer forward
                current_sum -= nums[left]
                left += 1
                
        # If min_length was never updated, it means no valid subarray was found
        return min_length if min_length != float('inf') else 0