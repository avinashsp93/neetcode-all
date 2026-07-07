# Trees

### Easy

- [094 - Binary Tree Inorder Traversal](#094---binary-tree-inorder-traversal)
- [100 - Same Tree](#0100---same-tree)
- [104 - Maximum Depth of Binary Tree](#0104---maximum-depth-of-binary-tree)
- [110 - Balanced Binary Tree](#0110---balanced-binary-tree)
- [144 - Binary Tree Preorder Traversal](#144---binary-tree-preorder-traversal)
- [145 - Binary Tree Postorder Traversal](#145---binary-tree-postorder-traversal)
- [543 - Diameter of Binary Tree](#0543---diameter-of-binary-tree)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

## 0100 - Same Tree

- **Problem:** Determine whether two binary trees are identical in both structure and node values.
- **Pattern:** `Binary Tree` / `Recursion`
- **Recognition:**
  - Two trees must be compared node by node.
  - Both the structure and values must match.
  - Recursion naturally traverses both trees simultaneously.
- **Key Insight:**
  - Compare the corresponding nodes of both trees:
    - If both are `None`, they match.
    - If only one is `None` or their values differ, the trees are different.
    - Otherwise, recursively compare their left and right subtrees.
  - The trees are the same only if every corresponding pair of nodes matches.

- **Time Complexity:** `O(n)`
  - `n` = number of nodes (assuming both trees have the same size)
- **Space Complexity:** `O(h)`
  - `h` = height of the tree (recursion stack)

### Example

```text
Input:

    1         1
   / \       / \
  2   3     2   3

Compare:
1 == 1 ✓
2 == 2 ✓
3 == 3 ✓

Output:
True
```

## 0104 - Maximum Depth of Binary Tree

- **Problem:** Return the maximum depth (height) of a binary tree.
- **Pattern:** `Binary Tree` / `Recursion`
- **Recognition:**
  - The depth of a node depends on the depths of its left and right subtrees.
  - Each subtree can be solved independently.
  - This naturally leads to a recursive solution.
- **Key Insight:**
  - If the current node is `None`, its depth is `0`.
  - Recursively compute the depths of the left and right subtrees.
  - The depth of the current node is:
    ```text
    max(leftDepth, rightDepth) + 1
    ```
  - The recursion returns the maximum depth of the entire tree.

- **Time Complexity:** `O(n)`
  - Every node is visited exactly once.
- **Space Complexity:** `O(h)`
  - `h` = height of the tree (recursion stack)

### Example

```text
Input:

      3
     / \
    9   20
       /  \
      15   7

Depths:
9  -> 1
20 -> 2
3  -> 3

Output:
3
```

## 0110 - Balanced Binary Tree

- **Problem:** Determine whether a binary tree is height-balanced, where the heights of the left and right subtrees of every node differ by at most `1`.
- **Pattern:** `Binary Tree` / `Recursion`
- **Recognition:**
  - Balance depends on both the heights and balance of the subtrees.
  - Computing height separately for every node would be inefficient.
  - A single post-order traversal can compute both simultaneously.
- **Key Insight:**
  - For each node, recursively obtain:
    - Whether the left subtree is balanced.
    - Whether the right subtree is balanced.
    - The heights of both subtrees.
  - The current node is balanced if:
    - Both subtrees are balanced.
    - Their heights differ by at most `1`.
  - Return both the balance status and the height to the parent.

- **Time Complexity:** `O(n)`
  - Each node is visited exactly once.
- **Space Complexity:** `O(h)`
  - `h` = height of the tree (recursion stack)

### Example

```text
Input:

      3
     / \
    9   20
       /  \
      15   7

Heights:
Left = 1
Right = 2

Difference:
|2 - 1| = 1

Output:
True
```

## 0543 - Diameter of Binary Tree

- **Problem:** Find the diameter of a binary tree, where the diameter is the number of edges on the longest path between any two nodes.
- **Pattern:** `Binary Tree` / `Recursion`
- **Recognition:**
  - The longest path may or may not pass through the root.
  - The diameter through a node equals the sum of the heights of its left and right subtrees.
  - A post-order traversal allows both height computation and diameter updates in one pass.
- **Key Insight:**
  - Recursively compute the heights of the left and right subtrees.
  - At each node:
    - Update the maximum diameter using:
      ```text
      leftHeight + rightHeight
      ```
    - Return the height of the current subtree:
      ```text
      max(leftHeight, rightHeight) + 1
      ```
  - The largest diameter encountered during the traversal is the final answer.

- **Time Complexity:** `O(n)`
  - Every node is visited exactly once.
- **Space Complexity:** `O(h)`
  - `h` = height of the tree (recursion stack)

### Example

```text
Input:

      1
     / \
    2   3
   / \
  4   5

Heights:
Node 2 -> 2
Node 3 -> 1

Diameter through root:
2 + 1 = 3

Output:
3
```

## 0572 - Subtree of Another Tree

- **Problem:** Determine whether one binary tree is a subtree of another.
- **Pattern:** `Binary Tree` / `Recursion`
- **Recognition:**
  - Need to compare entire subtrees, not just individual nodes.
  - Every node in the main tree is a potential root of the subtree.
  - A recursive tree comparison can verify structural equality.
- **Key Insight:**
  - Define a helper function to determine whether two trees are identical:
    - Both nodes are `None` → identical.
    - One node is `None` or values differ → not identical.
    - Otherwise, recursively compare both left and right children.
  - Traverse the main tree.
  - At each node:
    - Check if the subtree rooted there is identical to `subRoot`.
    - If not, recursively search the left and right subtrees.
  - Return `True` as soon as a matching subtree is found.

- **Time Complexity:** `O(m × n)`
  - `m` = number of nodes in `root`
  - `n` = number of nodes in `subRoot`
- **Space Complexity:** `O(h)`
  - `h` = height of the recursion stack

### Example

```text
Input:

Root:
      3
     / \
    4   5
   / \
  1   2

SubRoot:
    4
   / \
  1   2

Compare at each node:
3 ✗
4 ✓

Output:
True
```