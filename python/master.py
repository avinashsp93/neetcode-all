from typing import List
from l0_from_leetcode.d2_medium.p0054_spiral_matrix import Solution

def main() -> None:
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    result = Solution().spiralOrder(matrix)
    print("result:", result)

if __name__ == "__main__":
    main()