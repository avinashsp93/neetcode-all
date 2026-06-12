from typing import List
from l0_from_leetcode.d2_medium.p0074_search_a_2d_matrix import Solution
def main() -> None:
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 11
    result = Solution().searchMatrix(matrix, target)
    print(result)


if __name__ == "__main__":
    main()