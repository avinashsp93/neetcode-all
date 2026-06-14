# Linked List

### Easy

- [0021 - Merge Two Sorted Lists](#0021---merge-two-sorted-lists)
- [0083 - Remove Duplicates from Sorted List](#0083---remove-duplicates-from-sorted-list)
- [0141 - Linked List Cycle](#0141---linked-list-cycle)
- [0203 - Remove Linked List Elements](#0203---remove-linked-list-elements)
- [0206 - Reverse Linked List](#0206---reverse-linked-list)
- [0234 - Palindrome Linked List](#0234---palindrome-linked-list)
- [0876 - Middle of the Linked List](#0876---middle-of-the-linked-list)

### Hard

- [0023 - Merge K Sorted Lists](#0023---merge-k-sorted-lists)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

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

## 0083 - Remove Duplicates from Sorted List

- **Problem:** Remove duplicate nodes from a sorted linked list so that each value appears only once.
- **Pattern:** `Linked List`
- **Recognition:**
  - The list is already sorted.
  - Duplicate values appear consecutively.
  - Only adjacent nodes need to be compared.
- **Key Insight:**
  - Traverse the list using `prev` and `curr`.
  - If `curr.val == prev.val`, skip the duplicate node by updating:
    ```text
    prev.next = curr.next
    ```
  - Otherwise, move `prev` forward.
  - Since the list is sorted, all duplicates are adjacent and can be removed in a single pass.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
1 -> 1 -> 2 -> 3 -> 3

Remove duplicates:
1 -> 2 -> 3

Output:
1 -> 2 -> 3
```

## 0141 - Linked List Cycle

- **Problem:** Determine whether a linked list contains a cycle.
- **Pattern:** `Linked List` / `Fast & Slow Pointers`
- **Recognition:**
  - Need to detect whether traversal can loop indefinitely.
  - Revisiting a node indicates a cycle.
  - Can be solved either with extra memory (`Hash Set`) or in constant space (`Floyd's Algorithm`).

- **Key Insight (Hash Set):**
  - Traverse the list and store visited nodes in a set.
  - If a node is encountered again, a cycle exists.
  - Simple and intuitive, but requires extra space.

- **Key Insight (Floyd's Tortoise and Hare):**
  - Use two pointers:
    - `tortoise` moves one step at a time.
    - `hare` moves two steps at a time.
  - If a cycle exists, the fast pointer will eventually meet the slow pointer.
  - If the fast pointer reaches `None`, no cycle exists.
  - You could check for hare or hare.next being `None` upfront to avoid null pointer exceptions.

- **Time Complexity:** `O(n)`
- **Space Complexity:**
  - Hash Set: `O(n)`
  - Floyd's Algorithm: `O(1)`

### Example

```text
Input:
3 -> 2 -> 0 -> -4
     ^         |
     |_________|

Traversal loops back to node 2.

Output:
True
```

## 0203 - Remove Linked List Elements

- **Problem:** Remove all nodes from a linked list whose value equals `val`.
- **Pattern:** `Linked List`
- **Recognition:**
  - Nodes may need to be removed from anywhere in the list, including the head.
  - Deleting a node requires access to its previous node.
  - A dummy node simplifies edge cases involving the head.
- **Key Insight:**
  - Create a dummy node pointing to the head.
  - Use two pointers:
    - `prev` → last valid node
    - `curr` → current node being inspected
  - If `curr.val == val`, skip the node
  - Otherwise, move `prev` forward.
  - Return `dummy.next` as the new head.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
head = 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
val = 6

Remove all nodes with value 6:

1 -> 2 -> 3 -> 4 -> 5

Output:
1 -> 2 -> 3 -> 4 -> 5
```


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

## 0234 - Palindrome Linked List

- **Problem:** Determine whether a linked list reads the same forward and backward.
- **Pattern:** `Linked List` / `Fast & Slow Pointers`
- **Recognition:**
  - Need to compare the first half of the list with the second half.
  - Random access is unavailable in a linked list.
  - Reversing one half enables a direct node-by-node comparison.
- **Key Insight:**
  - Use slow and fast pointers to find the middle of the list.
  - Reverse the second half in-place.
  - Compare nodes from:
    - the start of the list
    - the head of the reversed second half
  - If all corresponding values match, the list is a palindrome.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
1 -> 2 -> 2 -> 1

Find middle:
1 -> 2 | 2 -> 1

Reverse second half:
1 -> 2 | 1 -> 2

Compare:
1 == 1 ✓
2 == 2 ✓

Output:
True
```

## 0876 - Middle of the Linked List

- **Problem:** Return the middle node of a linked list. If there are two middle nodes, return the second one.
- **Pattern:** `Linked List` / `Fast & Slow Pointers`
- **Recognition:**
  - Need to find a position relative to the length of the list.
  - Computing the length first is unnecessary.
  - Fast and slow pointers can locate the middle in one pass.
- **Key Insight:**
  - Use two pointers:
    - `tortoise` moves one node at a time.
    - `hare` moves two nodes at a time.
  - When `hare` reaches the end of the list, `tortoise` will be at the middle.
  - For even-length lists, this naturally returns the second middle node.
  - Let hare move first twice so that when it reaches the end, tortoise is at the correct middle node.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
[
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]

Merge first two:
1 -> 1 -> 3 -> 4 -> 4 -> 5

Merge with third:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Output:
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

- Note: A more optimal solution uses Divide & Conquer or a Min Heap, achieving O(N log k) time instead of O(Nk).d
1 -> 2 -> 3 -> 4 -> 5

Traversal:
tortoise moves 1 step
hare moves 2 steps

When hare reaches the end:
tortoise points to 3

Output:
3 -> 4 -> 5
```

<h2 style="text-align: center;text-transform: uppercase;">
  HARD PROBLEMS
</h2>

## 0023 - Merge K Sorted Lists

- **Problem:** Merge `k` sorted linked lists into one sorted linked list.
- **Pattern:** `Linked List` / `Iterative Merge`
- **Recognition:**
  - Multiple sorted lists need to be combined.
  - A known solution exists for merging two sorted lists.
  - Repeatedly applying the two-list merge can solve the larger problem.
- **Key Insight:**
  - Start with the first list as the current result.
  - Iteratively merge it with each remaining list using the standard two-pointer merge technique.
  - After each merge, the result remains sorted and becomes the input for the next merge.
  - Continue until all lists have been merged.

- **Time Complexity:** `O(Nk)`
  - `N` = total number of nodes across all lists
  - `k` = number of lists
  - Each merge may traverse most of the accumulated result.
- **Space Complexity:** `O(1)`
  - Nodes are reused; no additional linked lists are created.

