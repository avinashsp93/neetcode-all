from typing import List
from l0_from_leetcode.p0482_license_key_formatting import Solution

def main() -> None:
    # Input
    s = "5F3Z-2e-9-w"
    k = 2
    result = Solution().licenseKeyFormatting(s, k)
    print("result:", result)

if __name__ == "__main__":
    main()