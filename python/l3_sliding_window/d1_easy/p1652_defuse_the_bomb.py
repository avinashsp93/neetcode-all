from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for j in range(len(code))]

        left, right = 1, k+1
        if k < 0:
            left, right = k, 0
        
        runningSum = 0
        result = []
        for i in range(left, right):
            runningSum += code[i % len(code)]
        result.append(runningSum)

        if k > 0:
            for l in range(1, len(code)):
                runningSum -= code[l % len(code)]
                runningSum += code[(l + k) % len(code)]
                result.append(runningSum)
        else:
            for l in range(1, len(code)):
                runningSum += code[(l - 1) % len(code)]
                runningSum -= code[(l + k - 1) % len(code)]
                result.append(runningSum)
        return result


        