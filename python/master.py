from typing import List
from l0_from_leetcode.d2_medium.p0048_rotate_image import Solution

def main() -> None:
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = Solution().rotate(matrix)
    print("result:", result)

if __name__ == "__main__":
    main()