class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for w in sentences:
            m = max(m, w.count(" "))
        return m + 1