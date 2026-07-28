from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramToListDict = defaultdict(list)
        for anag in strs:
            anagKeyList = [0] * 26
            for c in anag:
                anagKeyList[ord(c) - ord("a")]+=1
            anagramToListDict[tuple(anagKeyList)].append(anag)
        return list(anagramToListDict.values())