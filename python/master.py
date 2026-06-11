from typing import List
from l0_from_leetcode.d2_medium.p0074_search_a_2d_matrix import Solution

def main() -> None:

    matrix = [
        [10, 20],
        [30, 40]
    ]
    target = 5

    result = Solution().searchMatrix(matrix, target)
    print(result)


if __name__ == "__main__":
    main()