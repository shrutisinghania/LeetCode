class Solution:
    def getSkyline(self, buildings):
        building_list = []
        for l, r, h in buildings:
            building_list.append((l, h))
            building_list.append((r, -h))

        building_list.sort(key = lambda x : (x[0], -x[1]))
        q = []
        heapq.heappush(q, 0)
        prev_max_height = -1
        res = []
        for building in building_list:
            if building[1] < 0:
                q.remove(building[1])
                heapq.heapify(q)
            else:
                heapq.heappush(q , -building[1])
            
            max_height = -q[0] if q[0] < 0 else 0

            if prev_max_height != max_height:
                res.append((building[0], max_height))
                prev_max_height = max_height
        return res
