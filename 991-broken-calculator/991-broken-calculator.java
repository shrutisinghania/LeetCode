class Solution {
    public int brokenCalc(int startValue, int target) {
        int ans = 0;
        while(startValue < target)
        {
            ans++;
            if(target % 2 == 0)
                target /= 2;
            else
                target++;
        }
        return ans + startValue - target;
    }
}