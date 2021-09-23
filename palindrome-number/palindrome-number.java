class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        int rem = 0, copy, rev = 0;
        copy = x;
        while (x!=0){
            rem = x % 10;
            rev = rev * 10 + rem;
            x = x / 10;
        }
        if (copy == rev)
            return true ;
        return false;
    }
}