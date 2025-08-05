class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        stack=[]
        def backtrack(ind,ans):
                stack.append(list(ans))
                for i in range(ind,len(nums)):
                    if i>ind and nums[i]==nums[i-1]:
                        continue
                    ans.append(nums[i])
                    backtrack(i+1,ans)
                    ans.pop()
        backtrack(0,[])
        return stack


            
        