from typing import List
from l3_linked_list.d1_easy.p0021_merge_two_sorted_lists import ListNode, Solution

def main() -> None:
    l1 = ListNode(1, ListNode(2, ListNode(4, ListNode(4, ListNode(6, None)))))
    l2 = ListNode(1, ListNode(3, ListNode(4, ListNode(5, None))))


    l3 = Solution().mergeTwoLists(l1, l2)

    while l3 is not None:
        print(l3.val)
        l3 = l3.next


if __name__ == "__main__":
    main()