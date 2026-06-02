from typing import List
import copy

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        charOccurences = dict()
        for i in chars:
            charOccurences[i] = charOccurences.get(i, 0) + 1
        
        for word in words:
            letOcr = dict()
            for k in word:
                letOcr[k] = letOcr.get(k, 0) + 1
            
            canWordBeFormed = True
            for k,v in letOcr.items():
                if charOccurences.get(k, 0) < v:
                    canWordBeFormed = False
                    break
            
            if canWordBeFormed:
                count+=len(word)

        return count
