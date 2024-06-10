class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        if n == 0:
            return True
        if (len(flowerbed) == 1):
            if flowerbed[0] == 0:
                return True
            else:
                return False
        

        for i in range(len(flowerbed)):
            if i > 1 and (i != len(flowerbed) - 1):
                if flowerbed[i] == 0:
                    if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                        count += 1
                        flowerbed[i] = 1
            elif i == 0:
                if flowerbed[i] == 0:
                    if flowerbed[i + 1] != 1:
                        count += 1
                        flowerbed[i] = 1
            else:
                if flowerbed[i] == 0:
                    if flowerbed[i - 1] != 1:
                        count += 1
                        flowerbed[i] = 1
        if n <= count:
            return True
        else:
            return False
        