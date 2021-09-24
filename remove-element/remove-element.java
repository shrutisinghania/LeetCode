class Solution {
    public int removeElement(int[] nums, int val) {
        int no = 0;
        int l = nums.length;
        for(int i = 0; i < l-no; i++){
            if(nums[i] == val ){ 
                no++;
                while(nums[l - no] == val && l-no != i)
                    no++;
                nums[i] = nums[l-no];
            }
        }
        return l-no;
    }
}