class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            found = True
            for char in word:
                if char not in allowed:
                    found = False
                    break
            if found == True:
                count += 1
        return count