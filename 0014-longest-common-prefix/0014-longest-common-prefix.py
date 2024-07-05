class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in strs[1:]:
            while i[:len(pre)] != pre: 
                pre = pre[:-1]
                if not pre:
                    return ""
        return pre
            