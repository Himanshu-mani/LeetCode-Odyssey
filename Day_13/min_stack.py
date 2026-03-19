# ==========================================================
# Question No: 155
# Title: Min Stack
# Level: Medium
# Time Complexity: O(1) for all operations (push, pop, top, getMin)
# Space Complexity: O(n) as we use an auxiliary 'min_stack'
# ==========================================================

class MinStack(object):

    def __init__(self):
        """
        Initialize your data structures here.
        """
        # Main stack to store all elements
        self.stack = []
        # Shadow stack to keep track of the minimum at each point
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        # Logic: If min_stack is empty, current val is the minimum.
        # Otherwise, compare current val with the top of min_stack.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # We store the smaller of (new value, current minimum)
            new_min = min(val, self.min_stack[-1])
            self.min_stack.append(new_min)

    def pop(self):
        """
        :rtype: None
        """
        # Both stacks must stay in sync to maintain the correct minimum
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Returns the last element added to the main stack
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # Returns the top of min_stack, which is always the minimum of the current stack
        return self.min_stack[-1]

# ==========================================================
# DRIVER CODE: How to use this class (Example)
# ==========================================================
# This part helps you test the code on your local machine.

if __name__ == "__main__":
    # 1. Initialize the stack machine
    obj = MinStack()
    
    # 2. Push elements
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    
    # 3. Get minimum (Should return -3)
    print("Current Minimum:", obj.getMin()) 
    
    # 4. Remove top element (-3)
    obj.pop()
    
    # 5. Check top (Should be 0)
    print("Top Element:", obj.top())         
    
    # 6. Get minimum again (Should now be -2)
    print("New Minimum after pop:", obj.getMin())