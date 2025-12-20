class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        for c in s:
            if stack and c in hash_map:
                l = stack.pop()
                if hash_map.get(c) != l:
                    return False
            else:
                stack.append(c)
        return not stack