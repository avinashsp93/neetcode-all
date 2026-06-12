from typing import List

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for i in encoded:
            decoded.append(i ^ decoded[-1])
        return decoded