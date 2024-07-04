class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        class Node:
            def __init__(self):
                self.childnode = [None] * 26
                self.end = False
                
                
        class Trie():
            def __init__(self):
                self.root = Node()
            
            def insert(self, s):
                cn = self.root
                for c in s.lower():
                    n = ord(c) - ord('a')
                    if not cn.childnode[n]:
                        cn.childnode[n] = Node()
                    cn = cn.childnode[n]
                cn.end = True
                    
            def lcs(self, s):
                cn = self.root
                sub = ""
                for c in s.lower():
                    n = ord(c) - ord('a')
                    if not cn.childnode[n] or cn.end:
                        return sub
                    cn = cn.childnode[n]
                    sub += c
                return sub
        
        t = Trie()
        t.insert(strs[0])
        s = strs[0]
        for i in strs[1:]:
            s = t.lcs(i)
            if not s or len(s) == 0:
                return ""
            t.insert(s)
        return s
            