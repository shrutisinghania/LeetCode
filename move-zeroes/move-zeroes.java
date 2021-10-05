class Solution {
    public void moveZeroes(int[] nums) {
        int swap = 0;
        for(int i =0; i < nums.length; i++)
        {
            if (nums[i] == 0 &&  i+1 < nums.length)
            {
                int j = i + 1, temp;
                while (nums[j] == 0 )
                {
                    j++;
                    if (j == nums.length)
                        return;
                }
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                swap++;
            }
        }
    }
}