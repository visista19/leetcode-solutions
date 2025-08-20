from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        longest = 0

        for i in num_set:
            if i - 1 not in num_set:  # start of a sequence
                x = i
                streak = 1
                while x + 1 in num_set:
                    x += 1
                    streak += 1
                longest = max(longest, streak)

        return longest
