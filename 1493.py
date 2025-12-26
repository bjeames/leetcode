class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        global_max = 0
        k = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k+=1
            while k > 1:
                if nums[l] == 0:
                    k-=1
                l+=1
            global_max = max(r-l, global_max)
            
        return global_max