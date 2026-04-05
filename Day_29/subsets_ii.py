"""
QUESTION: #90 Subsets II (Medium)
TIME COMPLEXITY: O(n * 2^n) - We generate 2^n subsets and copy each.
SPACE COMPLEXITY: O(n) - Space used by recursion stack.
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        # Sort to handle duplicates easily
        nums.sort()

        def backtrack(start, path):
            # Add current subset to result
            res.append(list(path))

            for i in range(start, len(nums)):
                # Skip duplicate numbers at the same level
                if i > start and nums[i] == nums[i-1]:
                    continue

                # Add number and move to next
                path.append(nums[i])
                backtrack(i + 1, path)
                # Remove number to try next option
                path.pop()

        backtrack(0, [])
        return res