class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        masterDict = dict()

        for char in chars:
            masterDict[char] = masterDict.get(char, 0) + 1

        result = 0
        for word in words:
            letterDict = dict()
            for letter in word:
                letterDict[letter] = letterDict.get(letter, 0) + 1
            
            found = True
            for k,v in letterDict.items():
                if k in masterDict and v <= masterDict[k]:
                    continue
                else:
                    found = False
            if found:
                result += len(word)
        return result