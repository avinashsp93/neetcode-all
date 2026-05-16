from typing import List
from l2_stack.p1598_crawler_log_folder import Solution
# from l1_arrays_and_hashing.p0205_isomorphic_strings import Solution

def main() -> None:
    # Input
    logs = ["d1/","d2/","./","d3/","../","d31/"]
    result = Solution().minOperations_stackApproach(logs)
    print("result:", result)

if __name__ == "__main__":
    main()