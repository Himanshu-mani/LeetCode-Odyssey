# Question No: 739
# Title: Daily Temperatures
# Level: Medium
# Time Complexity: O(n) - We visit each temperature once.
# Space Complexity: O(n) - We use a stack to store indices.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        # 1. Initialize result array with 0s
        # If no warmer day is found, the value stays 0.
        ans = [0] * n
        
        # 2. This stack will store the 'indices' of days waiting for a warmer day.
        stack = [] 

        for i in range(n):
            current_temp = temperatures[i]
            
            # 3. Check if today is warmer than the days in our stack (waitlist).
            # While the stack is not empty and current temperature is higher:
            while stack and current_temp > temperatures[stack[-1]]:
                # Pop the index of the previous cooler day
                prev_day_index = stack.pop()
                
                # Calculate how many days passed (Current Index - Old Index)
                ans[prev_day_index] = i - prev_day_index
            
            # 4. Add today's index to the stack to wait for a warmer day.
            stack.append(i)
            
        return ans