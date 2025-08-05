public class permu{
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>(); // FIXED: was 'new Array<>()'
        boolean[] freq = new boolean[nums.length];
        recurpermute(nums, ds, ans, freq);
        return ans;
    }

    private void recurpermute(int[] nums, List<Integer> ds, List<List<Integer>> ans, boolean[] freq) {
        if (ds.size() == nums.length) {
            ans.add(new ArrayList<>(ds)); // add a deep copy
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (!freq[i]) {
                freq[i] = true;
                ds.add(nums[i]);
                recurpermute(nums, ds, ans, freq);
                ds.remove(ds.size() - 1); // backtrack
                freq[i] = false;
            }
        }
    }
}
 
    

