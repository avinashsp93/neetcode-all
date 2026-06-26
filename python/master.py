from typing import List

from l3_sliding_window.d1_easy.p1652_defuse_the_bomb import Solution
def main() -> None:
    code = [2,4,9,3]
    k = -2
    result = Solution().decrypt(code, k)
    print(result)

if __name__ == "__main__":
    main()