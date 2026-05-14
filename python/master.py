from typing import List
from l1_arrays_and_hashing.p1800_maximum_ascending_subarray_sum import Solution

def main() -> None:
    # Input
    nums = [10,20,30,5,10,50]
    result = Solution().maxAscendingSum(nums)
    print("result:", result)

if __name__ == "__main__":
    main()