class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        first_max = 0
        for c in s[:k]:
            if c in vowels:
                first_max += 1

        left = 0 
        right = k

        local_max = first_max
        while right < len(s):
            if s[left] in vowels:
                local_max -= 1
            if s[right] in vowels:
                local_max += 1
            if local_max > first_max:
                first_max = local_max
            left += 1
            right += 1
        
        return first_max