class Solution:
    def clearDigits(self, s: str) -> str:
        charStack = []
        for i in s:
            if i.isdigit() and charStack and charStack[-1].isalpha():
                charStack.pop()
            else:
                charStack.append(i)
        return "".join(charStack)