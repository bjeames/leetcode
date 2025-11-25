class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s doesn't exist, return true, would want to clarify this. If s is an
        #empty string, could it be a valid subsequence?
        if not s:
            return True
        # if t doesn't exist, then it is impossible for something to be a substring of t
        if not t:
            return False
        # make s pointer
        s_pointer = 0
        # id how long s is, if s pointer makes it to that length, return true
        target = len(s)

        #iterate over each item of t, if t[i] = s[pointer], move both pointers forward, else
        # only move t pointer forward.
        for i in range(len(t)):
            if t[i] == s[s_pointer]:
                s_pointer += 1
            if s_pointer == target:
                return True
            
        return False