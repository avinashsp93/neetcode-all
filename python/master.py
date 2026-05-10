from typing import List
from l2_stack.p0020_valid_parentheses import Solution

def main() -> None:
    # Input
    s = "]][["

    result = Solution().isValid(s)
    print("result:", result)

if __name__ == "__main__":
    main()