class Solution {    
    public void reverseString(char[] s) {
        int l = 0, r = s.length - 1;
        while(l < r)
        {
            if (s[l] !=  s[r])
            {
                char temp  = s[l];
                s[l] = s[r];
                s[r] = temp;
            }
            l++;
            r--;
        }
    }
}