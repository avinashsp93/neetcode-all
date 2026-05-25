class Solution:
    def maxDifference(self, s: str) -> int:
        occurences_dict = dict()
        for i in s:
            occurences_dict[i] = occurences_dict.get(i, 0) + 1
        
        even_min, odd_max = float('inf'), 0
        for k,v in occurences_dict.items():
            if(v%2 == 0):
                if v < even_min:
                    even_min = v
            else:
                if v > odd_max:
                    odd_max = v
        return odd_max - even_min

