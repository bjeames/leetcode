class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        s_list = list(s)
        for i in range(len(t)):
            if t[i] == s_list[0]:
                s_list.pop(0)
                if len(s_list) == 0:
                    return True
                    
        return False