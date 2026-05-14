class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in operations:
            if i == "C":
                s.pop()
            elif i == "D":
                s.append(int(s[-1]) * 2)
            elif i == "+":
                s.append(int(s[-1]) + int(s[-2]))
            else:
                s.append(int(i))
        return sum(s)