class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = [[] for _ in range(numRows)]
        size = len(s)
        i = 0
        while i < size:
            j = 0
            while j < numRows:
                if i >= size:
                    break
                l[j].append(s[i])
                j += 1
                i += 1
            j = numRows - 2
            while j > 0:
                if i >= size:
                    break
                l[j].append(s[i])
                j -= 1
                i += 1 
        return "".join(str(item) for sublist in l for item in sublist)

