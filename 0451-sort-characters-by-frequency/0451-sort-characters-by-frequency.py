class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        s_d = dict(sorted(d.items(), key = lambda x : x[1], reverse= True))
        st = ''
        for key, value in s_d.items():
            st = st + str(key * value)
        return st