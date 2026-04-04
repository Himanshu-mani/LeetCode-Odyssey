# Question: 509. Fibonacci Number
# Type: Recursion with Memoization (Hash Map)
# Time Complexity: O(n) - Each number is calculated only once
# Space Complexity: O(n) - Recursion stack and Hash Map storage

class Solution(object):
    def fib(self, n):
        # Hash map to store already calculated values (Tijori)
        memo = {}

        def helper(num):
            # Base Cases
            if num == 0: return 0
            if num == 1: return 1
            
            # Check if answer is already in our Hash Map
            if num in memo:
                return memo[num]
            
            # Calculate and save the result in Hash Map
            memo[num] = helper(num - 1) + helper(num - 2)
            return memo[num]

        return helper(n)