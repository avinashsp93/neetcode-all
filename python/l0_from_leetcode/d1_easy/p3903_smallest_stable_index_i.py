class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minScores = []
        maxScores = []

        maxScore = nums[0]
        for i in nums:
            if i > maxScore:
                maxScore = i
            maxScores.append(maxScore)
        minScore = nums[len(nums) - 1]

        for j in nums[::-1]:
            if j < minScore:
                minScore = j
            minScores.append(minScore)
        minScores.reverse()

        result = -1
        for i in range(0, len(maxScores)):
            if (maxScores[i] - minScores[i]) <= k:
                if result == -1 or result > i:
                    result = i
        return result