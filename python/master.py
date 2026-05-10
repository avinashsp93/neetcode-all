from typing import List
# from arrays_and_hashing.p0001_two_sum import Solution
# from arrays_and_hashing.p0217_contains_duplicate import Solution
from arrays_and_hashing.p0242_valid_anagram import Solution

def main() -> None:
    # Input
    s = "rat"
    t = "car"

    result = Solution().isAnagram(s, t)
    print("containsDuplicate result:", result)

if __name__ == "__main__":
    main()
