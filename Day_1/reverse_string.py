# Problem: Reverse String (LeetCode 344)
# Approach: Two Pointers (In-place)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None (Modifies s in-place)
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swapping elements using Pythonic way
            s[left], s[right] = s[right], s[left]
            
            # Moving pointers towards each other
            left += 1
            right -= 1