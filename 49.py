class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for string in strs:
            temp = ''.join(sorted(string))
            if temp in hash_map:
                hash_map[temp].append(string)
            else:
                hash_map[temp] = [string]

        return list(hash_map.values())