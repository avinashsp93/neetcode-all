class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentenceArray = sentence.split(' ')
        for i in range(0, len(sentenceArray)):
            j = i - 1
            if(sentenceArray[i][0] != sentenceArray[j][-1]):
                return False
        return True