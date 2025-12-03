from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = Counter(p)
        l = 0
        r = l + len(p)
        res = []
        while r <= len(s):
            local_str = s[l:r]
            s_dict = Counter(local_str)
            if s_dict == p_dict:
                res.append(l)
            l += 1
            r+=1
        return res
