from typing import List
from l0_from_leetcode.d2_medium.p0165_compare_version_numbers import Solution

def main() -> None:
    version1 = "1.0.1"
    version2 = "1"
    result = Solution().compareVersion(version1, version2)
    print("result:", result)

if __name__ == "__main__":
    main()