class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        a = [0 for _ in range(n+1)]
        l= []
        for i in range(n):
            a[i+1] = a[i] ^ arr[i]

        for i, j in queries:
            l.append(a[i] ^ a[j+1])
        return l
