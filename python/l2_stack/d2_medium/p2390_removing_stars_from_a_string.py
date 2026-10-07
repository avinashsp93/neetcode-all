class Solution:
    def removeStars(self, s: str) -> str:
        charStack = []
        for ch in s:
            if ch == "*":
                charStack.pop()
            else:
                charStack.append(ch)
        return "".join(charStack)