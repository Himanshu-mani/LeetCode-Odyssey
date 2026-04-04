# Problem: Maximum Average Subarray I
# Difficulty: Easy
# Time Complexity: O(n) - Linear scan of the array
# Space Complexity: O(1) - Only constant extra space used

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Initialize the first window sum using slicing
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window from index k to the end of the array
        for i in range(k, len(nums)):
            # Update the window sum: Add current element and subtract the leftmost element
            current_sum += nums[i] - nums[i - k]
            
            # Update max_sum if current_sum is larger
            if current_sum > max_sum:
                max_sum = current_sum
                
        # Return the result as a float average
        return float(max_sum) / k