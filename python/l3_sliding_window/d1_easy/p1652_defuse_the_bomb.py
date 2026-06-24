class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        left, right = 1, k
        if k < 0:
            left, right = -1, k
            
        runningSum = 0

        if k == 0:
            return [0 for i in range(len(code))]

        result = []

        if k > 0:
            for i in range(left, right+1):
                runningSum += code[i]
        else:
            for i in range(left, right-1, -1):
                runningSum += code[i]
        
        for j in range(0, len(code)):
            result.append(runningSum)
            right += 1
            runningSum += code[right % len(code)]
            runningSum -= code[left % len(code)]
            left += 1
        
        return result