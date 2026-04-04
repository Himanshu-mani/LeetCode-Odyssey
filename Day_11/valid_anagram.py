# Day 11: Valid Anagram (LeetCode #242)
# Time Complexity: O(n) - We iterate through strings once.
# Space Complexity: O(1) - The map size is limited by the number of unique characters (26 for English alphabet).

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Dictionary to store character counts
        count_map = {}

        # Update counts: +1 for string 's', -1 for string 't'
        for i in range(len(s)):
            count_map[s[i]] = count_map.get(s[i], 0) + 1
            count_map[t[i]] = count_map.get(t[i], 0) - 1
            
        # If all counts are zero, they are valid anagrams
        for count in count_map.values():
            if count != 0:
                return False
                
        return True