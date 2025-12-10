class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        counter = {}

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            while (r-l+1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
                
            max_len = max(max_len, r-l+1)
        
        return max_len