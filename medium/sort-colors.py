class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = {0: 0, 1: 0, 2: 0}
        for i in nums:
            freq[i] += 1
        nums.clear()
        list0 = [0] * freq[0] + [1] * freq[1] + [2] * freq[2]
        nums.extend(list0)