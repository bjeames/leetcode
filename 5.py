class Solution:
    def longestPalindrome(self, s: str) -> str:   
        def is_pal(string:str):
            if string == string[::-1]:
                return True
            return False
        global_max = ''
        
        for i in range(len(s)):
            j = i+1
            while j <= len(s):
                target = s[i:j]
                if is_pal(target) and len(target) > len(global_max):
                    global_max = target
                j+=1
        
        return global_max