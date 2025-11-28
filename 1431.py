class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find max candies in candies list
        max_candies = max(candies)
        # res = []
        # # iterate over each item in candies
        # for item in candies:
        #     if item + extraCandies >= max_candies:
        #         res.append(True)
        #     else:
        #         res.append(False)
        # add the etrxa candies to the item
        # if the sum is greater than or equal to our max candies, append, else false

        #  modify the list in place?
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        return candies