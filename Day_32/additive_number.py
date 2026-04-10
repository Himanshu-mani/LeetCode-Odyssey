# Type: Sequence Split Pattern
# Difficulty: Medium
# Time Complexity: O(N^3)
# Space Complexity: O(N)

class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)

        def backtrack(n1, n2, start):
            # Base Case: Entire string validated
            if start == len(num): return True
            
            expected = str(int(n1) + int(n2))
            # Check if next part of string matches expected sum
            if not num.startswith(expected, start):
                return False
            
            # Move forward: current n2 becomes n1, expected becomes n2
            return backtrack(n2, expected, start + len(expected))

        # Nested loops to pick first two numbers
        for i in range(1, n):
            s1 = num[:i]
            if len(s1) > 1 and s1[0] == '0': break
            for j in range(i + 1, n):
                s2 = num[i:j]
                if len(s2) > 1 and s2[0] == '0': break
                # If these two can form a sequence, return True
                if backtrack(s1, s2, j): return True
        return False