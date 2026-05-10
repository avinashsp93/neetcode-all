from typing import List
# from arrays_and_hashing.p0001_two_sum import Solution
# from arrays_and_hashing.p0217_contains_duplicate import Solution
# from arrays_and_hashing.p0242_valid_anagram import Solution
# from arrays_and_hashing.p1299_replace_elements_with_greatest_element_on_right_side import Solution
# from arrays_and_hashing.p0392_is_subsequence import Solution
# from arrays_and_hashing.p2678_number_of_senior_citizens import Solution
# from arrays_and_hashing.p0485_max_consecutive_ones import Solution
# from arrays_and_hashing.p0929_unique_email_addresses import Solution
from arrays_and_hashing.p0014_longest_common_prefix import Solution


def main() -> None:
    # Input
    strs = ["dog","racecar","car"]

    result = Solution().longestCommonPrefix(strs)
    print("result:", result)

if __name__ == "__main__":
    main()
