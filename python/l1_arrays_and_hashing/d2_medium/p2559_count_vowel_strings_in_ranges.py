from itertools import accumulate

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        # convert words to binary array
        wordsBinaryArray = [1 if word[0] == word[-1] else 0 for word in words]
        print(wordsBinaryArray)
        prefixSumWordsBinaryArray = []
        numSum = 0
        for num in wordsBinaryArray:
            numSum += num
            prefixSumWordsBinaryArray.append(numSum)
        print(prefixSumWordsBinaryArray)

        for query in queries:    
            if query[0] == 0:
                result.append(prefixSumWordsBinaryArray[query[1]])
            else:
                result.append(prefixSumWordsBinaryArray[query[1]] - prefixSumWordsBinaryArray[query[0]-1])
        return result

    # Time limit exceeds - optimal solution is necessary
    def vowelStrings_bruteForce(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        for i in range(0, len(queries)):
            query = queries[i]
            count = 0
            for j in range(query[0], query[1]):
                if(words[j][0] == words[j][-1] and words[j][0] in "aeiou"):
                    count+=1
            result.append(count)
        return result