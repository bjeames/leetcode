class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        word1_dict = {}
        for item in word1:
            if item in word1_dict.keys():
                word1_dict[item] +=1
            else:
                word1_dict[item] = 1
        
        word2_dict = {}
        for item in word2:
            if item in word2_dict.keys():
                word2_dict[item] += 1
            else:
                word2_dict[item] = 1
        
        word1_val = list(sorted(word1_dict.values()))
        word2_val = list(sorted(word2_dict.values()))

        if word1_dict.keys() == word2_dict.keys() and word1_val == word2_val:
            return True
        
        return False


