class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. Sort is mandatory to handle duplicates and enable pruning
        candidates.sort()
        
        result = []
        path = []

        def backtrack(index, current_target):
            # Base Case: Success!
            if current_target == 0:
                result.append(path[:]) # Save a copy of current path
                return
            
            # Iterative Branching
            for i in range(index, len(candidates)):
                # 2. PRUNING: If current number > target, no need to check further 
                # because the array is sorted. This makes it super fast!
                if candidates[i] > current_target:
                    break
                
                # 3. SKIP DUPLICATES: Skip if the same value is used at the same level
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                # Action: Choose the number
                path.append(candidates[i])
                
                # Recurse: Move to next index (i + 1) because each number is used once
                backtrack(i + 1, current_target - candidates[i])
                
                # Backtrack: Remove the number to explore other branches
                path.pop()

        # Initial Call: Start from index 0 with full target
        backtrack(0, target)
        
        return result