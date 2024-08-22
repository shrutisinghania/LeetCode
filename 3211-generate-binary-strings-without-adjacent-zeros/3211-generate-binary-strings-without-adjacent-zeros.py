class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        def backtrack(l, s):
            if l == n:
                result.append(s)
                return
            if s[-1] == '0':
                backtrack(l+1, s+'1')
            else:
                backtrack(l+1, s+'1')
                backtrack(l+1, s+'0')
        backtrack(1, '1')
        backtrack(1, '0')
        return result