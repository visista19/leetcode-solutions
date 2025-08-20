class Solution {
    public int maxSubArray(int[] nums) {
        for (int i=0;i<nums.length;i++){
            int sum=0;
            int maxi=-99999;
            sum=sum+nums[i];
            if (maxi<sum){
                maxi=sum;
            }
            if (sum<0){
                sum=0;
            }
        }
        return maxi;
    }
}

// 🔎 Line-by-Line Explanation
// int sum = 0;

// sum is the running sum of the current subarray we are building.

// At first, it’s empty (0).

// int maxi = nums[0];

// maxi keeps track of the maximum subarray sum found so far.

// We start with the first element nums[0] because the array might contain negative numbers.
// (Example: if array = [-3,-2,-1], the answer should be -1, not 0).

// Loop: for (int i = 0; i < nums.length; i++)

// We iterate through every element of the array.

// sum = sum + nums[i];

// Add the current element to the running sum.

// This means:

// Either we continue the previous subarray by including nums[i]

// Or we start fresh later (if sum becomes negative).

// if (sum > maxi) maxi = sum;

// Check if the current running sum is the largest we’ve seen so far.

// If yes, update maxi.

// if (sum < 0) sum = 0;

// If running sum becomes negative, it won’t help in making future subarrays larger.

// So we reset it to 0 and start fresh from the next element.

// return maxi;

// After checking all subarrays, maxi will store the maximum subarray sum.

// 🔥 Example Walkthrough

// Input: [-2,1,-3,4,-1,2,1,-5,4]

// Step by step:

// Start: sum = 0, maxi = -2

// i=0 → sum = -2 → maxi = -2 → reset sum=0 (since <0)

// i=1 → sum = 0+1 = 1 → maxi = 1

// i=2 → sum = 1+(-3) = -2 → maxi = 1 → reset sum=0

// i=3 → sum = 0+4 = 4 → maxi = 4

// i=4 → sum = 4+(-1) = 3 → maxi = 4

// i=5 → sum = 3+2 = 5 → maxi = 5

// i=6 → sum = 5+1 = 6 → maxi = 6

// i=7 → sum = 6+(-5) = 1 → maxi = 6

// i=8 → sum = 1+4 = 5 → maxi = 6

// Final Answer: 6 (subarray [4, -1, 2, 1])

// ✨ Key Takeaways

// Kadane’s Algorithm runs in O(n) time and O(1) space.

// It works by:

// Keeping a running sum.

// Resetting when it becomes negative.

// Tracking the maximum sum seen so far.