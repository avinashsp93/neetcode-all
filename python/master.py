from typing import List
from l1_arrays_and_hashing.p2053_kth_distinct_string_in_an_array import Solution

def main() -> None:
    # Input
    arr = ["d","b","c","b","c","a"]
    k = 2
    result = Solution().kthDistinct(arr, k)
    print("result:", result)

if __name__ == "__main__":
    main()