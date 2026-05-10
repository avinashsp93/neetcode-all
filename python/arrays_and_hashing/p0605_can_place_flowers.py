from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # destructure the array
        morphedFlowerBed = [0, *flowerbed, 0]
        
        # so that you can peek 1 behind and one ahead while traversing
        plantedCount = 0
        for i in range(1, len(morphedFlowerBed) - 1):
            if(morphedFlowerBed[i-1] == 0 and morphedFlowerBed[i] == 0 and morphedFlowerBed[i+1] == 0):
                morphedFlowerBed[i] = 1
                plantedCount += 1
        
        # make sure you planted enough flowers
        return plantedCount >= n