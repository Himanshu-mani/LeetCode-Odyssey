'''
LEETCODE #239: Sliding Window Maximum
DIFFICULTY: Hard
TECHNIQUE: Monotonic Deque (Decreasing Order)

TIME COMPLEXITY: O(N) -> Each element is added and removed at most once.
SPACE COMPLEXITY: O(K) -> Deque stores at most K elements.
'''

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # Result list to store maximums
        res = []
        # Monotonic deque to store indices of elements
        dq = deque() 
        
        for right in range(len(nums)):
            # Phase 1: Cleaning - Remove indices of smaller elements from back
            # Because they can never be the maximum if a larger element exists
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            
            # Phase 2: Entry - Add current element's index to the back
            dq.append(right)
            
            # Phase 3: Expiry - Remove index from front if it is outside the window
            if dq[0] < right - k + 1:
                dq.popleft()
            
            # Phase 4: Result - Once the first window is full, add max to result
            # The maximum is always at the front of our deque
            if right >= k - 1:
                res.append(nums[dq[0]])
                
        return res