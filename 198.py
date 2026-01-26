class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0 

        # [rob1, rob2, num1, num2,...]
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return dp[i]
        
        return dfs(0)
    
class Solution:
    def rob(self, nums: List[int]) -> int:

        dp ={}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(nums[i]+dfs(i+2), dfs(i+1))
            return dp[i]
        
        return dfs(0)

        
        