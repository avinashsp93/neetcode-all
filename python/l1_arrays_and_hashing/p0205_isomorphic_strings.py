class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        char_map = dict()
        rev_char_map = dict()

        for i in range(0, len(s)):
            if(s[i] not in char_map):
                char_map[s[i]] = t[i]
            else:
                if(char_map[s[i]] != t[i]):
                    return False
            if(t[i] not in rev_char_map):
                rev_char_map[t[i]] = s[i]
            else:
                if(rev_char_map[t[i]] != s[i]):
                    return False
            
        return True