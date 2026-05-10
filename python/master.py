from typing import List
from arrays_and_hashing.p0027_remove_element import Solution

def main() -> None:
    # Input
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    result = Solution().removeElement(nums, val)
    print("result:", result)

if __name__ == "__main__":
    main()