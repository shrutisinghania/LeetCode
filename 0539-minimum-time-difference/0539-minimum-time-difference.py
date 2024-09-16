class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def conv_to_min(time):
            hour, minute = time.split(':')
            return int(hour) * 60 + int(minute)

        timePoints_min = [conv_to_min(time) for time in timePoints]
        timePoints_min.sort()
        diff = []
        min_diff = 1440 - timePoints_min[-1] + timePoints_min[0]

        for i in range(1, len(timePoints_min)):
            min_diff = min(min_diff, timePoints_min[i] - timePoints_min[i-1])

        return min_diff

