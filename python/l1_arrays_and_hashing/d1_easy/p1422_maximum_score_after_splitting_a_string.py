class Solution:
    def maxScore(self, s: str) -> int:
        leftScore, rightScore = s[0].count('0'), s[1:].count('1')
        currentTotal = leftScore + rightScore
        maxTotal = currentTotal
        for i in range(1, len(s)-1):
            if s[i] == '0':
                leftScore += 1
                currentTotal += 1
            else:
                rightScore -= 1
                currentTotal -= 1
            maxTotal = max(maxTotal, currentTotal)
        return maxTotal