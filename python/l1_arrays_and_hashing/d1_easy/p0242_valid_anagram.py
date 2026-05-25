class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # input precheck
        if len(s) != len(t):
            return False

        my_dict_letter_to_word = dict()

        # smarter insert
        for i in s:
            my_dict_letter_to_word[i] = my_dict_letter_to_word.get(i, 0) + 1
        
        for j in t:
            if j in my_dict_letter_to_word:
                my_dict_letter_to_word[j] -= 1
            else:
                return False
        
        # use of all/any
        return all(v == 0 for v in my_dict_letter_to_word.values())