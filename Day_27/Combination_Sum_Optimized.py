class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. Sort the candidates to enable PRUNING (Early Exit)
        # This is the secret to 0ms runtime.
        candidates.sort()
        
        result = []
        path = []

        def backtrack(current_target, index):
            # SUCCESS CASE: If target is reached
            if current_target == 0:
                # Store a copy of the path (the combination found)
                result.append(path[:])
                return

            # LOOP through candidates starting from the current index
            for i in range(index, len(candidates)):
                # 2. PRUNING: If the current number is already greater than 
                # the remaining target, no need to check further numbers.
                if candidates[i] > current_target:
                    break
                
                # Action: Pick the current candidate
                path.append(candidates[i])
                
                # Recurse: Try picking the same number again (index 'i' stays same)
                # This handles the "Unlimited Supply" logic.
                backtrack(current_target - candidates[i], i)
                
                # Backtrack: Remove the number to explore other options
                path.pop()

        # Start the recursion engine with full target and index 0
        backtrack(target, 0)
        
        return result