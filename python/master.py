from typing import List
from arrays_and_hashing.p0001_two_sum import Solution

def main() -> None:
    nums = [2, 7, 11, 15]
    target = 9

    result = Solution().twoSum(nums, target)
    print("twoSum result:", result)

if __name__ == "__main__":
    main()