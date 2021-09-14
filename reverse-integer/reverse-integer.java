class Solution {
    public int reverse(int x) {
        int rem = 0,r,p=0;
        while(x!=0){
            r = x % 10;
            rem = rem * 10 + r;
            if ((rem-r)/10 != p)
            {
                return 0;
            }
            p = rem;
            x = x / 10;
        }
        return rem;
    }
}