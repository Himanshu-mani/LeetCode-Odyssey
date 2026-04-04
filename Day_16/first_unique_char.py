# Question No: 387
# Title: First Unique Character in a String
# Level: Easy
# Time Complexity: O(n) - Two passes over the string
# Space Complexity: O(1) - Max 26 characters in the hash map

from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Count the frequency of each character
        count = Counter(s)
        
        # Step 2: Find the first character with frequency 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        # Step 3: If no unique character exists
        return -1