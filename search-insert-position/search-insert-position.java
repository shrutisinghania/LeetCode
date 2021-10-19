class Solution {
    public int searchInsert(int[] nums, int target) {
        int l = 0;
        int u = nums.length - 1;
        while (u - l > 1)
        {
            int i = l + (u - l)/2;
            if (nums[i] == target)
                return i;
            if (nums[i] < target)
                l = i;
            else
                u = i;
        }
        if (target == nums[u])
            return u;
        if (target <= nums[l])
            return l;
        if (target > nums[u])
            return u+1;
        return l+1;
    }
}