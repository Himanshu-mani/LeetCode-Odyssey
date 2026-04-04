# =========================================================================
# Question: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Topic: Hash Set & Array
# -------------------------------------------------------------------------
# Time Complexity: O(n) - We visit each number at most twice.
# Space Complexity: O(n) - We store all numbers in a Hash Set for O(1) lookup.
# =========================================================================

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. Edge Case: If the list is empty, the longest streak is 0.
        if not nums:
            return 0

        # 2. Convert the list to a Set to make lookups O(1).
        # This is the secret to getting O(n) overall time.
        num_set = set(nums)
        longest_streak = 0

        # 3. Iterate through the unique numbers in the set.
        for n in num_set:
            
            # 4. Identification Logic (Find the "Hero" / Start of a sequence).
            # If (n - 1) is not in the set, then 'n' must be the start of a sequence.
            if (n - 1) not in num_set:
                current_num = n
                current_streak = 1

                # 5. Counting Logic: Keep checking for the next numbers in the sequence.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # 6. Update the global maximum streak after the while loop finishes.
                # This ensures we handle single-element sequences correctly.
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Example Usage:
# sol = Solution()
# print(sol.longestConsecutive([100, 4, 200, 1, 3, 2])) # Output: 4 (for [1, 2, 3, 4])