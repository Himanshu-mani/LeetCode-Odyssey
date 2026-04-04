# Problem: Valid Palindrome (LeetCode 125)
# Approach: Two Pointers with Alphanumeric check
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters in lowercase
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True