class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c = 0
        highest = 0
        for g in gain:
            c += g
            if c > highest:
                highest = c
        return highest