class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largestSubString = "0"
        for i in range(0, len(num)-2):
            j = i+3
            subString = num[i:j]
            if subString[0] == subString[1] and subString[1] == subString[2]:
                if largestSubString == "0":
                    largestSubString = subString
                else:
                    if(int(largestSubString) < int(subString)):
                        largestSubString = subString
        return largestSubString if largestSubString != "0" else ""