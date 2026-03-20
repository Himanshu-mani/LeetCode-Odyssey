# Question No: 150
# Title: Evaluate Reverse Polish Notation (RPN)
# Level: Medium
# Time Complexity: O(n) -> We process each token exactly once.
# Space Complexity: O(n) -> In the worst case, we store all numbers in the stack.

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            # Step 1: Check if the token is a number or an operator
            if token not in "+-*/":
                # Convert string to integer and push to stack
                stack.append(int(token))
            
            else: 
                # Step 2: Operator found - Pop the two most recent operands
                # Remember: First pop is 'b', second pop is 'a'
                b = stack.pop()
                a = stack.pop()

                # Step 3: Perform the operation based on the operator
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Engineering Trick: Use float division and int() 
                    # to ensure truncation toward zero for negative results.
                    result = int(float(a) / b)
                    stack.append(result)

        # Step 4: The final result is the only element left in the stack
        return stack[0]