class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        wordDict = set(wordDict)

        def dfs(word):
            if word == '':
                return True
            if word in dp:
                return dp[word]

            cur = ''
            for i in range(len(word)):
                cur += word[i]
                if cur in wordDict:
                    if dfs(word[i+1:]):
                        dp[word] = True
                        return True
            dp[word] = False

            return dp[word]

        return dfs(s)
            
            


            

        