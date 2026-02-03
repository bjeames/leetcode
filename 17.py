class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        look_up = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def dfs(i,string):
            if i == len(digits):
                res.append(string)
                return
            for option in look_up[digits[i]]:
                dfs(i+1,string+option)
        
        dfs(0, '')

        return res