class Solution:
    def longestPalindrome(self, s: str) -> str:
        def center_pal(s, l, r):
            while l>=0 and r < len(s) and l <= r and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        st = 0
        en = 0
        max_pal = 0
        for i in range(len(s)):
            o = center_pal(s, i, i)
            e = center_pal(s, i, i+1)
            max_pal = max(o, e)

            if en-st < max_pal:
                st = i - ((max_pal-1)//2)
                en = i + (max_pal//2)
        return s[st:en+1]
                