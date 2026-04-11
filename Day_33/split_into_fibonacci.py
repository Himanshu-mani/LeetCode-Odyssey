'''''
Question Number: 842
Name: Split Array into Fibonacci Sequence
Difficulty Level: Medium
Type: Backtracking / String Partitioning
Time Complexity: O(N * log^2 M)
Space Complexity: O(N)
'''''

class Solution(object):
    def splitIntoFibonacci(self, num):
        res = []

        def backtrack(index):
            # If we reached the end of the string and have at least 3 numbers, it's a success
            if index == len(num) and len(res) >= 3:
                return True
            
            for end in range(index, len(num)):
                segment = num[index: end + 1]
                val = int(segment)

                # Numbers like "01" or "05" are not allowed, only "0" is fine
                if segment[0] == '0' and len(segment) > 1:
                    break
                
                # The number must not exceed the 32-bit integer limit
                if val > 2 ** 31 - 1:
                    break
                
                if len(res) >= 2:
                    expected_sum = res[-1] + res[-2]
                    # If current number is smaller than sum, we need more digits, so continue
                    if val < expected_sum:
                        continue
                    # If current number is already bigger than sum, no need to check further
                    if val > expected_sum:
                        break
                
                # Add the number to our sequence and move forward
                res.append(val)
                if backtrack(end + 1):
                    return True
                
                # If path failed, remove the number and try a different split
                res.pop()
                
            return False
            
        backtrack(0)
        return res