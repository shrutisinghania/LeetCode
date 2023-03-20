class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0 ):
                    flowerbed[i] = 1
                    c += 1
            if c >= n:
                return True
        return False
            