from typing import List
# from arrays_and_hashing.p0001_two_sum import Solution
# from arrays_and_hashing.p0217_contains_duplicate import Solution
# from arrays_and_hashing.p0242_valid_anagram import Solution
# from arrays_and_hashing.p1299_replace_elements_with_greatest_element_on_right_side import Solution
from arrays_and_hashing.p392_is_subsequence import Solution

def main() -> None:
    # Input
    # arr = [17,18,5,4,6,1]
    s = "abc"
    t = "ahbgdc"

    result = Solution().isSubsequence(s,t)
    print("result:", result)

if __name__ == "__main__":
    main()
