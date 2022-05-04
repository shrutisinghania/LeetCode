class Solution {
    public int maxOperations(int[] nums, int k) {
        HashMap<Integer,Integer>map=new HashMap<>();
        int count=0;
        for(int i=0;i<nums.length;i++)
        {
            if(map.getOrDefault(k-nums[i], 0) > 0)
            {
                count++;
                map.put(k-nums[i], map.get(k-nums[i]) - 1);
            }
            else 
                map.put(nums[i], map.getOrDefault(nums[i],0)+1);
        }
        return count;
    }
}