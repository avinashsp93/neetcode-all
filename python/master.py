from typing import List
from l1_arrays_and_hashing.p0448_find_all_numbers_disappeared_in_an_array import Solution

def main() -> None:
    # Input
    nums = [4,3,2,7,8,2,3,1]
    # nums = [1,1]
    # nums = [1,4,4,4]


    result = Solution().findDisappearedNumbers(nums)
    print("result:", result)

if __name__ == "__main__":
    main()