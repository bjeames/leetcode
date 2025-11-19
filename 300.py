class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # instantiate dynamic programming array to store results
        dp = [1] * len(nums)

        # iterate over each value in nums
        for i in range(len(nums)):
            #iterate over every value that comes before nums[i]
            for j in range(i):
                #check if nums[i] is greater than any of its predecessors
                ## to see if it can continue the ascent
                if nums[i] > nums[j]:
                    # you need the max here because as the number of j's gets big
                    # it is possible that there will be mulitple values are less than
                    # nums[i] but some of them may come from longer sequences than 
                    # others.
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)