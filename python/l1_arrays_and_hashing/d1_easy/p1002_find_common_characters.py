class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        listOfWordCounts = []
        result = []

        if len(words) == 1:
            return list(words[0])

        for word in words:
            wordCount = dict()
            for char in word:
                wordCount[char] = wordCount.get(char, 0) + 1
            listOfWordCounts.append(wordCount)
        

        resultDict = dict()
        for key, value in listOfWordCounts[0].items():
            minValue = value
            for wordCountDict in listOfWordCounts[1:]:
                if key in wordCountDict:
                    minValue = min(minValue, wordCountDict[key])
                    resultDict[key] = minValue
                else:
                    resultDict.pop(key, None)
                    break
        
        for key, value in resultDict.items():
            for j in range(value):
                result.append(key)
        
        return result