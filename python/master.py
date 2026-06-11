from typing import List
from l3_linked_list.d1_easy.p0234_palindrome_linked_list import Solution, ListNode
def main() -> None:

    l1 = ListNode(1, ListNode(2, None))

    result = Solution().isPalindrome(l1)
    print(result)


if __name__ == "__main__":
    main()