import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        for c in s:
            if c.isalnum():
                new_string+=c.lower()
        l=0
        r=len(new_string)-1
        while r>l:
            if new_string[l] != new_string[r]:
                return False
            l += 1
            r -= 1
        return True