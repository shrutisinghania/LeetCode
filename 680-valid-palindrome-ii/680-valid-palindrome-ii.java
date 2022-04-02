class Solution {
    public boolean validPalindrome(String s) {
        return isPalindrome(s, 0, s.length() -1, true);
    }
    
    private boolean isPalindrome(String s, int l, int r, boolean val)
    {
        while(l < r)
        {
            if (s.charAt(l) != s.charAt(r))
            {
                if(val)
                    return (isPalindrome(s, l+1, r, false) || isPalindrome(s, l, r-1, false));
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
}