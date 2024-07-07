class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for l in range(len(haystack)):
            if haystack[l] == needle[0] and haystack[l:l + len(needle)] == needle:
                    return l