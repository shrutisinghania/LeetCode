class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for strt, end in intervals[1:]:
            if strt <= res[-1][1]:
                if res[-1][1] < end:
                    res[-1][1] = end
            else:
                res.append([strt, end])
        return res
     