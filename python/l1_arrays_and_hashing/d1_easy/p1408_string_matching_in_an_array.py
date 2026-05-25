from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subStrings = set()
        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                if(len(words[i]) > len(words[j])):
                    if(words[j] in words[i]):
                        subStrings.add(words[j])
                else:
                    if(words[i] in words[j]):
                        subStrings.add(words[i])
        return list(subStrings)
    
    # Could also be solved using Rabin-Karp algorithm, but the above solution is simpler for easy problems. Rabin-Karp would be more efficient for larger inputs.
