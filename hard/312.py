class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Add 1 to both ends
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Step 2: Initialize DP table
        dp = [[0] * n for _ in range(n)]
        
        # Step 3: Fill DP table by length of range
        for length in range(2, n):  # length is gap between left and right
            for left in range(0, n - length):
                right = left + length
                # Try bursting each balloon last in this range
                for k in range(left + 1, right):
                    coins = nums[left] * nums[k] * nums[right]
                    coins += dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
        
        # Step 4: Answer is bursting all balloons between 0 and n-1
        return dp[0][n - 1]

        