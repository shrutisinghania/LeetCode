class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in set(s):
            d[i] = s.count(i)
        s_d = dict(sorted(d.items(), key = lambda x : x[1], reverse= True))
        st = ''
        for key, value in s_d.items():
            st = st + str(key * value)
        return st