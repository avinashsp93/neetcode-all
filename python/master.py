from typing import List
from arrays_and_hashing.p1408_string_matching_in_an_array import Solution

def main() -> None:
    # Input
    words = ["leetcoder","leetcode","od","hamlet","am"]

    result = Solution().stringMatching(words)
    print("result:", result)

if __name__ == "__main__":
    main()