from typing import List
from l1_arrays_and_hashing.p0724_find_pivot_index import Solution

def main() -> None:
    # Input
    nums = [1,-1,2]
    result = Solution().pivotIndex(nums)
    print("result:", result)

if __name__ == "__main__":
    main()