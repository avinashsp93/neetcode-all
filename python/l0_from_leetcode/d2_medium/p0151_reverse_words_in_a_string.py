class Solution:
    def reverseWords(self, s: str) -> str:
        clean_text = " ".join(s.split())
        return " ".join(clean_text.split()[::-1])