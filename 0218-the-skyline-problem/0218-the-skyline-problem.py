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
        height_dict = {}
        height_dict[0] = 1
        for building in building_list:
            if building[1] > 0:
                heapq.heappush(q , -building[1])
                height_dict[building[1]] = height_dict.get(building[1], 0) + 1
            else:
                height_dict[-building[1]] -= 1
            
            max_height = -q[0] if q[0] < 0 else 0
            while q and height_dict[max_height] == 0:
                heapq.heappop(q)
                max_height = -q[0] if q[0] < 0 else 0

            if prev_max_height != max_height:
                res.append((building[0], max_height))
                prev_max_height = max_height
        return res
