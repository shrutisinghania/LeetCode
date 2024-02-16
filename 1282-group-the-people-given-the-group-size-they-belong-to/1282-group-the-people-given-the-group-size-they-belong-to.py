class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        a = []
        l = defaultdict(list)
        for ind, val in enumerate(groupSizes):
            l[val].append(ind)
            if len(l[val]) == val:
                a.append(l.pop(val))
        return a