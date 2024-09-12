class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        g = defaultdict(list)
        for i,j in edges:
            g[i].append(j)
            g[j].append(i)
        if target == 1 and 1 <= t  and len(g[1]) == 0:
            return 1

        q = [(1, 1, 0)]
        visited = set()
        visited.add(1)

        while q:
            node, prob, time = q.pop(0)
            l = len(g[node])
            if node != 1:
                l -= 1
            if l == 0:
                l = 1
            p = 1/l
            new_p = prob * p
            for n in g[node]:
                if n in visited:
                    continue
                if n == target :
                    if time + 1 == t or (time + 1 < t  and len(g[n]) == 1):
                        return new_p
                    return 0
                
                q.append((n, new_p, time+1))
                visited.add(n)
                if time + 1 > t:
                    return 0
        return 0
