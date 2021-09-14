class Solution {
    public int[] twoSum(int[] nums, int target) {
        int no;
        int[] myArray;
        myArray = new int[2];
        int l = nums.length;
        for(int i = 0; i < l; i++){
            no = target - nums[i];
            int index = i+1;
            while(index<l){
                if (nums[index] == no){
                    myArray[0] = i;
                    myArray[1] = index;
                    return myArray;
                }
                index+=1;
            }
        }
        return myArray;
    }
}