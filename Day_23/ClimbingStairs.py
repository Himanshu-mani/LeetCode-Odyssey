# Question: 70. Climbing Stairs
# Type: Dynamic Programming / Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def climbStairs(self, n):
        # Using a Hash Map (Dictionary) for speed boost
        memo = {}

        def solve(steps):
            # Base Cases: 1 way for 1 step, 2 ways for 2 steps
            if steps == 1: return 1
            if steps == 2: return 2
            
            # If we already know the answer for these steps, return it
            if steps in memo:
                return memo[steps]
            
            # Relation: Ways to reach N = Ways(N-1) + Ways(N-2)
            memo[steps] = solve(steps - 1) + solve(steps - 2)
            return memo[steps]

        return solve(n)