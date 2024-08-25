class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def createGraph():
            g = [[]  for _ in range(numCourses)]
            ind = [0] * numCourses
            for i in prerequisites:
                g[i[1]].append(i[0])
                ind[i[0]] += 1
            return g, ind

        g, ind = createGraph()
        q = []
        for inp, i in enumerate(ind):
            if i == 0:
                q.append(inp)
        v = []
        while q:
            c = q.pop(0)
            v.append(c)
            for i in g[c]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        return numCourses == len(v)



        