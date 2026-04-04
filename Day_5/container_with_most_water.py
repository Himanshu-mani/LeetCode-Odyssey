# Problem: Container With Most Water (LeetCode #11)
# Difficulty: Medium
# Technique: Two Pointers (Greedy)
# Time Complexity: O(n) - Single pass through the array.
# Space Complexity: O(1) - Constant space used.

class Solution(object):
    def maxArea(self, height):
        """
        Finds the maximum area of water a container can store.
        Uses two pointers starting from both ends to maximize width.
        
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        # Two-pointer approach to find the max area in O(n)
        while left < right:
            # 1. Height is determined by the shorter wall
            h = min(height[left], height[right])
            
            # 2. Width is the distance between the two pointers
            w = right - left
            
            # 3. Update the maximum area found so far
            max_area = max(max_area, h * w)
            
            # 4. Greedy Move: Move the pointer pointing to the shorter wall
            # This is because moving the taller wall won't help increase the height,
            # but moving the shorter wall might find a taller one.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area