public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int num = n;
        int count = 0;
        while(num != 0){
            int mask = num & (-num);
            num = num - mask;
            count++;
        }
        return count;
    }
}