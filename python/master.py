from typing import List
from l0_from_leetcode.d1_easy.p1886_determine_whether_matrix_can_be_obtained_by_rotation import Solution

def main() -> None:
    matrix = [[0,0],[1,0]]
    target = [[1,0],[0,0]]

    # matrix = [
    #     [1,0,0,0],
    #     [1,1,1,1],
    #     [0,0,1,0],
    #     [0,0,0,1],
    # ]
    # target = [
    #     [0,1,1,0],
    #     [1,0,0,1],
    #     [1,0,0,1],
    #     [0,1,1,0],
    # ]
    result = Solution().findRotation(matrix, target)
    print("result:", result)

if __name__ == "__main__":
    main()