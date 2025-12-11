# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n  # search in [l, r]

        while l <= r:
            mid = l + (r - l) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:  # mid is higher than pick
                r = mid - 1
            else:            # res == 1, mid is lower than pick
                l = mid + 1

        # Problem guarantees a solution, so we should never get here
        return -1
