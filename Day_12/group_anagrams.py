from collections import defaultdict

# Question No: 49
# Title: Group Anagrams
# Level: Medium
# Time Complexity: O(n * k log k) -> n is number of strings, k is max string length.
# Space Complexity: O(n * k) -> to store all strings in the hash map.

class Solution(object):
    def groupAnagrams(self, strs):
        # We use defaultdict(list) so we don't have to check if a key exists manually.
        # It automatically creates an empty list [] for any new key.
        ans = defaultdict(list)

        for s in strs:
            # Step 1: Sort the string to get a unique key (Signature).
            # Example: "eat", "tea", "ate" all become "aet" when sorted.
            key = "".join(sorted(s))
            
            # Step 2: Add the original string to the list belonging to that key.
            ans[key].append(s)

        # Step 3: Return only the grouped values from the dictionary.
        return ans.values()