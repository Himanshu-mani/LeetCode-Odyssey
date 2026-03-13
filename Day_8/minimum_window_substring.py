'''
LEETCODE #76: Minimum Window Substring
DIFFICULTY: Hard
TECHNIQUE: Optimized Sliding Window (Two Pointers + Frequency Map)

TIME COMPLEXITY: O(N + M) -> N is length of 's', M is length of 't'.
SPACE COMPLEXITY: O(K)    -> 'K' is the number of unique characters in 't'.
'''

class Solution(object):
    def minWindow(self, s, t):
        # Base Case: Agar string khali hai toh return empty string
        if not s or not t:
            return ""

        # Step 1: Target requirements ka map (count_t)
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Step 2: Current window tracking aur pointers
        window = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")
        left = 0

        # Step 3: Right pointer se window ko expand karo
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Agar basket mein kisi character ki ginti poori ho gayi
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # Step 4: Jab window 'Valid' ho jaye (have == need), use shrink karo
            while have == need:
                # Sabse choti window ka record update karo
                if (right - left + 1) < res_len:
                    res_len = (right - left + 1)
                    res = [left, right]

                # Left pointer wala character nikaal kar window choti karo
                left_char = s[left]
                window[left_char] -= 1
                
                # Agar nikaalne se requirement toot gayi, toh 'have' kam karo
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                left += 1

        # Step 5: Final substring return karo
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""
    

