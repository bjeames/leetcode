class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create a list to store the result
        res = [1] * len(nums)
        # track the current left product
        l = 1
        # track the current right product
        r = 1
        # iterate from left to right, store product of every num to the left of current index
        # start at index = 1 so you can use i - 1
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * l
            l = res[i]
        # iterate from right to left, multiply result by the right product
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * r
            r = r * nums[i]
        # return result
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i]*=postfix
            postfix*=nums[i]
        
        return res