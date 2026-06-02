from typing import List
from l0_from_leetcode.d2_medium.p0034_find_first_and_last_position_of_element_in_sorted_array import Solution

def main() -> None:
    nums = [1,2]
    target = 2

    result = Solution().searchRange(nums, target)
    print("result:", result)

if __name__ == "__main__":
    main()