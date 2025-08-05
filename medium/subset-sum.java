import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public ArrayList<Integer> subsetSums(int[] arr) {
        int N = arr.length;  
        ArrayList<Integer> subsetSum = new ArrayList<>();
        func(0, 0, arr, N, subsetSum);
        Collections.sort(subsetSum);
        return subsetSum;
    }
    void func(int ind, int sum, int[] arr, int N, ArrayList<Integer> subsetSum) {
        if (ind == N) {
            subsetSum.add(sum);
            return;
        }
        func(ind + 1, sum + arr[ind], arr, N, subsetSum);  // Fix: use arr[ind], not get.arr(ind)
        func(ind + 1, sum, arr, N, subsetSum);
    }
}
