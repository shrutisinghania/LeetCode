class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        l = []
        for ind, e in enumerate(s):
            if e == '(':
                st.append(('(',ind))
            elif e == ')':
                if not st:
                    l.append(ind)
                else:
                    st.pop()
        for i in st:
            l.append(i[1])
        for i in sorted(l, reverse=True):
            s = s[:i] + s[i + 1:]

        return s

                