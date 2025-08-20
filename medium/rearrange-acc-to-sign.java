import java.util.Arrays;

class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] ans= new int[nums.length];
        int negindex=1;
        int posindex=0;
        for(int i=0;i<nums.length;i++){
            if (nums[i]<0){
                ans[negindex]=nums[i];
                negindex+=2;
            }
            else {
                ans[posindex]=nums[i];
                posindex+=2;
            }
        }
        return ans;
    }
    public static void main(String[] args){
        Solution obj = new Solution();
        int[] result = obj.rearrangeArray(new int[]{2,1,-5,3,-2,-1});
        System.out.println(Arrays.toString(result));

    }
}
