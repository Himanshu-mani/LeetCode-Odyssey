# =========================================================================
# Question: 560. Subarray Sum Equals K
# Difficulty: Medium
# Topic: Hash Map & Prefix Sum
# -------------------------------------------------------------------------
# Time Complexity: O(n) - We traverse the array only once.
# Space Complexity: O(n) - We store prefix sums in a Hash Map.
# =========================================================================

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1. Initialize variables
        ans = 0
        curr_sum = 0
        
        # 2. The Dictionary (Diary) to store Prefix Sum frequencies.
        # Base Case: {0: 1} handles the case when curr_sum itself equals k.
        prev_map = {0: 1}
        
        for i in nums:
            # 3. Step A: Update the running total (Prefix Sum)
            curr_sum += i
            
            # 4. Step B: Calculate the target gap we need to find
            target = curr_sum - k
            
            # 5. Step C: If the target exists in our diary, it means 
            # we found subarrays that sum up to k.
            if target in prev_map:
                ans += prev_map[target]
            
            # 6. Step D: Register the current sum in the diary.
            # If it's new, set frequency to 1. If it exists, increment it.
            if curr_sum in prev_map:
                prev_map[curr_sum] += 1
            else:
                prev_map[curr_sum] = 1
                
        return ans

# Example Usage:
# sol = Solution()
# print(sol.subarraySum([1, 1, 1], 2)) # Output: 2