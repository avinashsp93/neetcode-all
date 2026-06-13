from typing import List
from python.l3_linked_list.d3_hard.p0023_merge_k_sorted_lists import ListNode, Solution
def main() -> None:
    
    l1 = ListNode(1, ListNode(4, ListNode(5, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    l3 = ListNode(2, ListNode(6, None))

    lists = [l1, l2, l3]

    Solution().mergeKLists(lists)


if __name__ == "__main__":
    main()