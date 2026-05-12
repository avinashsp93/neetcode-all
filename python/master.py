from typing import List
from l1_arrays_and_hashing.p0169_majority_element import Solution

def main() -> None:
    # Input
    nums = [0,0,0,1,1]
    result = Solution().majorityElement_onePass(nums)
    print("result:", result)

if __name__ == "__main__":
    main()