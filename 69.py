class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = 0
        r = x//2
        ans = 0

        while l <= r:
            mid = (l+r)//2

            if mid*mid <= x: # just right or too small
                ans = mid
                l = mid + 1
            if mid*mid > x: # too large
                r = mid -1

        return ans





        

        