class Solution:
    def maxArea(self, height: List[int]) -> int:
        global_max = 0
        l = 0
        r = len(height) -1
        while l<r:
            local_max = min(height[l], height[r])*(r-l)
            global_max = max(global_max, local_max)

            if height[l]> height[r]:
                r-=1
            else:
                l+=1
        return global_max