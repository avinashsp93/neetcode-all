class Solution:
    # safe solution but inefficient
    def majorityElement_bruteForce(self, nums: List[int]) -> List[int]:
        occurenceDict = dict()
        times = len(nums)//3
        result = []
        for num in nums:
            occurenceDict[num] = occurenceDict.get(num, 0) + 1

        for key, val in occurenceDict.items():
            if val > times:
                result.append(key)
        return result

    # Boyer-Moore Algorithm implemented without dictionary (candidates counts approach)
    def majorityElement_candidateCountApproach(self, nums: List[int]) -> List[int]:
        candidate1, candidate2, count1, count2 = None, None, 0, 0

        # Find candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # Find counts of candidates
        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Append candidates to the result, if they occur more than a 3rd
        result = []
        if count1 > len(nums)//3:
            result.append(candidate1)
        if count2 > len(nums)//3:
            result.append(candidate2)
        return result

    # could be slightly inefficient but does work
    def majorityElement_onePass_withDict(self, nums: List[int]) -> List[int]:
        occurenceDict = defaultdict(int)

        for num in nums:
            occurenceDict[num] += 1

            if len(occurenceDict.keys()) > 2:
                for ele in occurenceDict.keys():
                    occurenceDict[ele] -= 1

                occurenceDictCopy = defaultdict(int)
                for key, val in occurenceDict.items():
                    if val > 0:
                        occurenceDictCopy[key] = val

                occurenceDict = occurenceDictCopy

        result = []
        for key, val in occurenceDict.items():
            if nums.count(key) > len(nums)//3:
                result.append(key)
        return result