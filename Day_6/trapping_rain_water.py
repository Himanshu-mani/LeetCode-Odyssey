# Problem: Trapping Rain Water (LeetCode #42)
# Difficulty: Hard
# Technique: Two Pointers (Optimal O(1) Space)

class Solution(object):
    def trap(self, height):
        """
        Calculates trapped rainwater using two pointers.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0
        
        while left < right:
            # Greedy Choice: Always process the side with the smaller wall
            # because the amount of water is limited by the shorter boundary.
            if height[left] < height[right]:
                # Update left_max and calculate water at current index
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
                left += 1
            else:
                # Update right_max and calculate water at current index
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                right -= 1
                
        return total_water