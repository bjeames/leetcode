class Solution:
    def climbStairs(self, n: int) -> int:
        # check for edge cases before the algorithm starts
        if n <= 2:
            return n
            
        # algorithm equation:
        #ways(n) = ways(n-1) + ways(n-2)

        # starts out as ways(1), ways(2)
        # iteratively updates in the for loop to:
        # ways(2), ways(3)
        # ways(4), ways(5)
        ways_a, ways_b = 1, 2

        for _ in range(3, n+1):
            ways_a, ways_b = ways_b, ways_a + ways_b
            # ways_1, ways_2 = ways_2, ways_1 + ways_2
        return ways_b
