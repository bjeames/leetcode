
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        #check each index position in flowerbed, 
        # if the positon is a 0, and the previous and next positions are also 0, decrease n by 1
        # if n == 0, return True, else False
        # edge cases:
        # the first index will not have a previous, so it automatically has a zero to the left
        # the last index will not have a next, so it automatically has a zero to the right
        m = len(flowerbed)
        # if there are no flowers to place
        if n == 0:
            return True
        # if I don't have a flower bed
        if m == 0:
            return False

        for i in range(m):
            # check previous
            if (i == 0 or flowerbed[i-1] == 0):
                    #check next
                    if (i == m-1 or flowerbed[i+1] == 0):
                        #check current
                        if flowerbed[i] == 0:
                            flowerbed[i] = 1
                            n -= 1
                            if n == 0:
                                return True

        return False 



