from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sourceSet = set()
        for path in paths:
            source = path[0]
            sourceSet.add(source)

        for path in paths:
            if(path[1] not in sourceSet):
                return path[1]
        
        return ""

            