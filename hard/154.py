class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid  # Min is in left half including mid
            elif nums[mid] > nums[right]:
                left = mid + 1  # Min is in right half
            else:
                right -= 1  # Can't decide, reduce right by 1
        return nums[left]
