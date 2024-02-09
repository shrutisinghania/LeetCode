class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for ind, i in enumerate(words):
            if x in i:
                ans.append(ind)
        return ans
        