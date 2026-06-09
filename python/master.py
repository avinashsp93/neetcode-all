from typing import List
from l3_linked_list.d1_easy.reverse_linked_list import ListNode, Solution

def main() -> None:
    l1 = ListNode(1, None)
    l2 = ListNode(2, None)
    l3 = ListNode(3, None)
    l4 = ListNode(4, None)

    l1.next = l2
    l2.next = l3
    l3.next = l4

    head = l1

    Solution().reverseListRecursive(head)


if __name__ == "__main__":
    main()