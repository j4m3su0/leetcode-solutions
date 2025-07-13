class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n > len(flowerbed):
            return False

        if len(flowerbed) == 1 and 0 in flowerbed:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and n > 0:
                if i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    flowerbed [i] = 1
                    n -= 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1

        return n == 0
                
