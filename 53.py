class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum+=num
            global_max = max(curr_sum, global_max)
            curr_sum = max(0, curr_sum)
        return global_max
 

