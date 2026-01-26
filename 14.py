class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            target = strs[0][i]
            for word in strs:
                if word[i] != target:
                    return strs[0][:i]

        return strs[0][:min_len]