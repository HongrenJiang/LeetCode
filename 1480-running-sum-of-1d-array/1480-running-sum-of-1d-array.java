class Solution {
    public int[] runningSum(int[] nums) {
        int N = nums.length;
        int[] runningSum = new int[N];
        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += nums[i];
            runningSum[i] = sum;
        }
        
        return runningSum;
    }
}