# Linked List

### Easy

- [0021 - Merge Two Sorted Lists](#0021---merge-two-sorted-lists)
- [0206 - Reverse Linked List](#0206---reverse-linked-list)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

## 0206 - Reverse Linked List

- **Problem:** Reverse a singly linked list and return the new head.
- **Pattern:** `Linked List` / `Pointer Manipulation`
- **Recognition:**
  - Need to reverse the direction of all links in a linked list.
  - Requires updating pointers without losing access to the remaining nodes.
  - Can be solved efficiently using three pointers.
- **Key Insight:**
  - Maintain three pointers:
    - `prev` → previously processed node
    - `curr` → current node being processed
    - `nxt` → next node to preserve the remaining list
  - For each node:
    1. Save `curr.next` in `nxt`
    2. Reverse the link: `curr.next = prev`
    3. Move `prev` and `curr` forward
  - After processing all nodes, `prev` points to the new head of the reversed list.

- **Time Complexity:** `O(n)`
  - Each node is visited exactly once.
- **Space Complexity:** `O(1)`
  - Reversal is performed in-place.

### Example

```text
Input:
1 -> 2 -> 3 -> 4 -> 5

Iteration 1:
1 -> None

Iteration 2:
2 -> 1 -> None

Iteration 3:
3 -> 2 -> 1 -> None

Iteration 4:
4 -> 3 -> 2 -> 1 -> None

Iteration 5:
5 -> 4 -> 3 -> 2 -> 1 -> None

Output:
5 -> 4 -> 3 -> 2 -> 1
```

## 0021 - Merge Two Sorted Lists

- **Problem:** Merge two sorted linked lists into a single sorted linked list and return its head.
- **Pattern:** `Linked List` / `Two Pointers`
- **Recognition:**
  - Two sorted sequences need to be combined while maintaining sorted order.
  - Only the current node from each list needs to be compared.
  - A dummy node simplifies handling the head of the merged list.
- **Key Insight:**
  - Use a dummy node to build the merged list.
  - Maintain a `tail` pointer representing the last node in the merged list.
  - Compare the current nodes of both lists:
    - Append the smaller node to the merged list.
    - Advance the corresponding list pointer.
  - Once one list is exhausted, append the remaining nodes of the other list.
  - Return `dummy.next` as the head of the merged list.

- **Time Complexity:** `O(n + m)`
  - `n` and `m` are the lengths of the two lists.
- **Space Complexity:** `O(1)`
  - Nodes are reused; no additional list is created.

### Example

```text
Input:
list1 = 1 -> 2 -> 4
list2 = 1 -> 3 -> 4

Merge:
1 -> 1 -> 2 -> 3 -> 4 -> 4

Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4
```
