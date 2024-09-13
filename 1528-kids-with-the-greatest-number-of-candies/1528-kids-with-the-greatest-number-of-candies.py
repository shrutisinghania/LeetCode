class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        a = []
        for i in candies:
            a.append(i + extraCandies >= m)
        return a