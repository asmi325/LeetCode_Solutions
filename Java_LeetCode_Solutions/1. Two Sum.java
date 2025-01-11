class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i,j;
        int[] ans= new int[2];
        int start=o;
        int end= nums.length-1;

        while(start<end){
            int sum= nums[start]+nums[end];
            if(sum==target){
                ans[0]=start;
                ans[1]=end;
            }
            else if(sum>target){
                end--;
            }
            else{
                start++;
            }
        }
        
    }
    return ans;
}
