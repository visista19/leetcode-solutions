class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = {0: 0, 1: 0, 2: 0}
        for i in nums:
            freq[i] += 1
        nums.clear()
        list0 = [0] * freq[0] + [1] * freq[1] + [2] * freq[2]
        nums.extend(list0)
# another approach (optimal approach with time complexity: O(N) and space complexity: O(1))
# class Solution:
#     def sortColors(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         low=0
#         mid=0
#         high=len(arr)-1
#         while(mid<=high):
#             if arr[mid]==0:
#                 arr[low],arr[mid]=arr[mid],arr[low]
#                 low+=1
#                 mid+=1
#             elif arr[mid]==1:
#                 mid+=1
#             else:
#                 arr[mid],arr[high]=arr[high],arr[mid]
#                 high-=1
#         return arr
        