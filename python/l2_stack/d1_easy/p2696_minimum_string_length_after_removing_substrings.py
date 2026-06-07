class Solution:
    def minLength(self, s: str) -> int:
        charStack = []
        for i in s:
            if i == "B":
                if charStack and charStack[-1] == "A":
                    charStack.pop()
                else:
                    charStack.append(i)
            elif i == "D":
                if charStack and charStack[-1] == "C":
                    charStack.pop()
                else:
                    charStack.append(i)
            else:
                charStack.append(i)
        return len(charStack)