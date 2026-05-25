class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        listOfWords = s.split(' ')
        if len(pattern) != len(listOfWords):
            return False
        
        letterToWordDict = dict()
        wordToLetterDict = dict()
        for i in range(0, len(pattern)):
            # Map -> letter : word
            if pattern[i] not in letterToWordDict:
                letterToWordDict[pattern[i]] = listOfWords[i]
            else:
                if letterToWordDict[pattern[i]] != listOfWords[i]:
                    return False

            # Reverse Map -> word : letter
            if listOfWords[i] not in wordToLetterDict:
                wordToLetterDict[listOfWords[i]] = pattern[i]
            else:
                if wordToLetterDict[listOfWords[i]] != pattern[i]:
                    return False
        return True

