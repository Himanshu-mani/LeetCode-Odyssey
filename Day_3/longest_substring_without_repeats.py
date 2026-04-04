# Problem: Longest Substring Without Repeating Characters (LeetCode #3)
# Difficulty: Medium
# Time Complexity: O(n) - Each character is visited at most twice
# Space Complexity: O(min(m, n)) - Set size depends on the number of unique characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Finds the length of the longest substring without repeating characters 
        using the Sliding Window technique and a Hash Set.
        
        :type s: str
        :rtype: int
        """
        char_set = set()  # To store unique characters in the current window
        left = 0          # Left pointer of the window
        max_length = 0    # To track the maximum length found so far
        
        # Iterate through the string with the 'right' pointer
        for right in range(len(s)):
            # If a duplicate is found, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set and expand the window
            char_set.add(s[right])
            
            # Update the maximum length: window size is (right - left + 1)
            max_length = max(max_length, right - left + 1)
            
        return max_length