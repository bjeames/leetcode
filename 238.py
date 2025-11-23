class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        current_prod = 1
        current_suffix = 1

        #left to right:
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * current_prod
            current_prod = res[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * current_suffix
            current_suffix *= nums[i]