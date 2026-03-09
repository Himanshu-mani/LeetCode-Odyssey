# Problem: 3Sum (LeetCode #15)
# Difficulty: Medium
# Technique: Sorting + Two Pointers
# Time Complexity: O(n^2) - One loop for 'i', and an internal 'while' for two pointers.
# Space Complexity: O(1) or O(n) - Depending on the internal sorting algorithm's space.

class Solution(object):
    def threeSum(self, nums):
        """
        Finds all unique triplets in the array that sum up to zero.
        Uses a sorted array and two-pointer technique to achieve O(n^2) efficiency.
        
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Step 1: Sort the array to handle duplicates and use pointers effectively
        nums.sort()
        result = []
        n = len(nums)

        # Step 2: Iterate through the array, fixing one number 'i'
        for i in range(n - 2):
            # Skip duplicate values for 'i' to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Step 3: Initialize Left and Right pointers
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Target found! Add to result
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Step 4: Skip duplicates for 'left' and 'right' pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers to fresh elements
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    # Sum is too small, increase it by moving left pointer forward
                    left += 1
                else:
                    # Sum is too large, decrease it by moving right pointer backward
                    right -= 1
                    
        return result