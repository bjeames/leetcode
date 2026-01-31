from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        l = 0
        r = len(s1)

        while r <= len(s2):
            if s1_counts == Counter(s2[l:r]):
                return True
            l+=1
            r+=1
        
        return False

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_array = [0]*26
        for c in s1:
            s1_array[ord(c) - ord('a')] += 1
        
        s2_array = [0]*26
        l = 0
        r = 0
        while r < len(s2):
            s2_array[ord(s2[r])-ord('a')] +=1
            if r >= len(s1):
                s2_array[ord(s2[l]) - ord('a')] -= 1
                l+=1
                r+=1
            if r < len(s1):
                r+=1
            if s2_array == s1_array:
                return True
        
        return False