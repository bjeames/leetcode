class Solution:
    def reverseVowels(self, s: str) -> str:
        # do I have to maintain case? upper/lower?

        #make vowels list
        #iterate over string
            #stack vowels
            #save indexes
        #for each index, make string index equal top of stack

        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', "I", "O", 'U']
        stack = []
        indexes = []
        s_list = list(s)

        for i in range(len(s)):
            if s[i] in v:
                stack.append(s[i])
                indexes.append(i)
        for i in indexes:
            s_list[i] = stack.pop()
        
        return ''.join(s_list)

        

        