class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums)-1
        counter = 0

        while left < right:
            if sorted_nums[left] + sorted_nums[right] == k:
                counter+=1
                left+=1
                right-=1
            elif sorted_nums[left] + sorted_nums[right] < k:
                left+=1
            else:
                right -=1
        
        return counter