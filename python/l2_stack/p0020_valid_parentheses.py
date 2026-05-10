class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brace_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif i in [')','}',']']:
                if not stack or brace_map[i] != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True