# Linked List

### Easy

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
