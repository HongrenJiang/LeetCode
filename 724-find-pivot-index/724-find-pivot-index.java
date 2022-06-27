class Solution {
    public int leftSum(int[] nums, int index) {
        int N = nums.length;
        int leftSum = 0;
        for (int i = 0; (i < index) && (i < N) ; i++) {
            leftSum += nums[i];
        }
        
        return leftSum;
    }
    
    public int rightSum(int[] nums, int index) {
        int N = nums.length;
        int rightSum = 0;
        for (int i = index + 1;  i < N; i++) {
            rightSum += nums[i];
        }
        
        return rightSum;
    }
    
    public int pivotIndex(int[] nums) {
        int N = nums.length;
        for (int i = 0; i < N; i++) {
            int left = leftSum(nums, i);
            //System.out.println(left);
            int right = rightSum(nums, i);
            //System.out.println(right);
            if (left == right) {
                return i;
            }
        }
        
        return -1;
    }
}