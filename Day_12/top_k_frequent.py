from collections import Counter

# Question No: 347
# Title: Top K Frequent Elements
# Level: Medium
# Time Complexity: O(n) -> We iterate through the array and buckets in linear time.
# Space Complexity: O(n) -> For the frequency map and the bucket list.

class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Count how many times each number appears (Frequency Map).
        count = Counter(nums)
        
        # Step 2: Use Bucket Sort logic. 
        # Create a list where the index represents the frequency.
        # Index 3 will store numbers that appeared 3 times.
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for n, freq in count.items():
            buckets[freq].append(n)
            
        res = []
        # Step 3: Iterate through the buckets from back to front (Highest frequency first).
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                # Step 4: Once we have k elements, we are done.
                if len(res) == k:
                    return res