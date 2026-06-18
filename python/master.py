from typing import List
from l0_from_leetcode.d2_medium.p0033_search_in_rotated_sorted_array import Solution
def main() -> None:
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = Solution().search(nums, target)

    
    print(result)

if __name__ == "__main__":
    main()