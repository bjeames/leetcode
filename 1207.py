class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # create seen map by iterating over each item in arr that stores each items count
        # compare the list of the dictionary's values to its set
        # if they match return true (i.e. each count is unique)
        # if they don't match return false (i.e. the set notation removed at least 1 duplicate)

        seen = {}

        for num in arr:
            if num not in seen.keys():
                seen[num] = 1
            else:
                seen[num] += 1
        
        set_len = len(set(seen.values()))
        
        return set_len == len(seen.values())