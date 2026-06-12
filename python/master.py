from typing import List
from l0_from_leetcode.d2_medium.p3895_count_digit_appearances import Solution
def main() -> None:
    nums = [0,54]
    digit = 0
    result = Solution().countDigitOccurrences(nums, digit)
    print(result)


if __name__ == "__main__":
    main()