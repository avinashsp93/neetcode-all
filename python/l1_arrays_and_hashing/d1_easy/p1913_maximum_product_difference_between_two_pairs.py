class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest, secondLargest = 0, 0
        smallest, secondSmallest = float('inf'), float('inf')
        for i in nums:
            if i > secondLargest:
                secondLargest = i
                if i > largest:
                    secondLargest = largest
                    largest = i
            if i < secondSmallest:
                secondSmallest = i
                if i < smallest:
                    secondSmallest = smallest
                    smallest = i
        return largest * secondLargest - secondSmallest * smallest
