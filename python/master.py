from typing import List
from l1_arrays_and_hashing.p0290_word_pattern import Solution
# from l1_arrays_and_hashing.p0205_isomorphic_strings import Solution

def main() -> None:
    # Input
    pattern = "aaaa"
    s = "dog dog dog dog"
    # pattern = "abba"
    # s = "aaaa"
    result = Solution().wordPattern(pattern, s)
    print("result:", result)

if __name__ == "__main__":
    main()