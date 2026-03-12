
''' 
Problem: Longest Repeating Character Replacement (LeetCode #424)
Difficulty: Medium
Technique: Sliding Window (Variable Size)
 
TIME COMPLEXITY: O(n) -> Where 'n' is the length of string 's'. Each character is visited at most twice (by right & left pointers).
SPACE COMPLEXITY: O(1) -> We use a hash map to store counts of at most 26 uppercase English letters, which is constant space.
 '''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}  # Dictionary to store frequency of characters in the current window
        left = 0
        max_freq = 0      # Stores the frequency of the most common character in the window
        max_length = 0    #  Maximum valid window size found
        
        for right in range(len(s)):
            # 1. Expand the window by adding the current character
            char = s[right]
            char_counts[char] = char_counts.get(char, 0) + 1
            
            # 2. Update the max_freq if the current character's count is higher
            max_freq = max(max_freq, char_counts[char])
            
            # 3. Calculate how many replacements are needed for the current window
            # replacements_needed = (Window Size) - (Count of most frequent char)
            replacements_needed = (right - left + 1) - max_freq
            
            # 4. If replacements needed > k, the window is invalid. Shrink it!
            if replacements_needed > k:
                # Remove the leftmost character's effect from our memory
                char_counts[s[left]] -= 1
                left += 1
            
            # 5. Capture the maximum valid window size seen so far
            # After the 'if' block, we are guaranteed to have a valid window.
            max_length = max(max_length, right - left + 1)
            
        return max_length