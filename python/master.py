from typing import List
from l3_linked_list.d1_easy.p0203_remove_linked_list_elements import Solution, ListNode
def main() -> None:
    head = ListNode(7, ListNode(7, ListNode(7, ListNode(7, None))))
    val = 7
    result = Solution().removeElements(head, val)
    print(result)


if __name__ == "__main__":
    main()