class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = 0
        max_w = 0
        s_i = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d.keys() and d[s[i]] >= s_i:
                s_i = d[s[i]] + 1
                w = i - s_i + 1
                d[s[i]] = i
            else:
                w += 1
                d[s[i]] = i
            max_w = max(w, max_w)
        return max_w