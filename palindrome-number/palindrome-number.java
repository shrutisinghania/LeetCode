class Solution {
    public boolean isPalindrome(int x) {
        int rem = 0, copy, rev = 0;
        copy = x;
        while (x!=0){
            rem = x % 10;
            rem = (rem < 0) ? -rem : rem;
            rev = rev * 10 + rem;
            x = x / 10;
        }
        if (copy == rev)
            return true ;
        return false;
    }
}