class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1[::-1])
        word2 = list(word2[::-1])
        output = ''
        while word1 or word2:
            if word1:
                output += word1.pop()
            if word2:
                output += word2.pop()
        return output