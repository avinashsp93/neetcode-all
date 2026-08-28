class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        charCount = dict()
        for word in words:
            for letter in word:
                charCount[letter] = charCount.get(letter, 0) + 1

        for k,v in charCount.items():
            if v % len(words) != 0:
                return False
        return True