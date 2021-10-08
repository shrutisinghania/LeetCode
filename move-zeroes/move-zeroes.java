class Solution {
    public void moveZeroes(int[] nums) {
        for(int i =0; i < nums.length; i++)
        {
            if (nums[i] == 0 &&  i+1 < nums.length)
            {
                int j = i + 1;
                while (nums[j] == 0 )
                {
                    j++;
                    if (j == nums.length)
                        return;
                }
                exchange(nums, i, j);
            }
        }
    }
    
    private void exchange(int[] nums, int i, int j)
    {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}