class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def cnt(a):
            c = 0
            for i in a:
                if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    c += 1
            return c
        
        l = len(s)//2
        return (cnt(s[:l]) == cnt(s[l:]))
        
        
                      
        