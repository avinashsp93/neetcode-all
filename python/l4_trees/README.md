# Trees

### Easy

- [0094 - Binary Tree Inorder Traversal](#0094---binary-tree-inorder-traversal)
- [0100 - Same Tree](#0100---same-tree)
- [0104 - Maximum Depth of Binary Tree](#0104---maximum-depth-of-binary-tree)
- [0108 - Convert Sorted Array to Binary Search Tree](#0108---convert-sorted-array-to-binary-search-tree)
- [0110 - Balanced Binary Tree](#0110---balanced-binary-tree)
- [0144 - Binary Tree Preorder Traversal](#0144---binary-tree-preorder-traversal)
- [0145 - Binary Tree Postorder Traversal](#0145---binary-tree-postorder-traversal)
- [0226 - Invert Binary Tree](#0226---invert-binary-tree)
- [0543 - Diameter of Binary Tree](#0543---diameter-of-binary-tree)
- [0589 - N-ary Tree Preorder Traversal](#0589---n-ary-tree-preorder-traversal)
- [0590 - N-ary Tree Postorder Traversal](#0590---n-ary-tree-postorder-traversal)
- [2331 - Evaluate Boolean Binary Tree](#2331---evaluate-boolean-binary-tree)

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

## 0108 - Convert Sorted Array to Binary Search Tree

- **Problem:** Convert a sorted array into a height-balanced Binary Search Tree (BST).
- **Pattern:** `Binary Tree` / `Divide and Conquer`
- **Recognition:**
  - The input array is already sorted.
  - The middle element naturally becomes the root of a balanced BST.
  - The left and right halves recursively form the left and right subtrees.
- **Key Insight:**
  - Recursively build the tree:
    - Choose the middle element as the root.
    - Build the left subtree from the left half of the array.
    - Build the right subtree from the right half of the array.
  - Stop recursion when the subarray becomes empty.
  - Choosing the middle element at every step keeps the BST height-balanced.

- **Time Complexity:** `O(n)`
  - Every element is used exactly once to create a tree node.
- **Space Complexity:** `O(log n)`
  - Due to the recursion stack for a balanced tree.

### Example

```text
Input:
nums = [-10, -3, 0, 5, 9]

Choose middle:
        0
      /   \
    -10    5
      \     \
      -3     9

Output:
Height-balanced BST
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

## 0226 - Invert Binary Tree

- **Problem:** Invert a binary tree by swapping the left and right child of every node.
- **Pattern:** `Binary Tree` / `Recursion`
- **Recognition:**
  - Every node is processed independently.
  - The same operation (swap children) is applied recursively to each subtree.
  - A depth-first traversal naturally visits every node.
- **Key Insight:**
  - If the current node is `None`, stop recursion.
  - Swap the left and right children of the current node.
  - Recursively invert the left and right subtrees.
  - After every node has been processed, the entire tree is inverted.

- **Time Complexity:** `O(n)`
  - Every node is visited exactly once.
- **Space Complexity:** `O(h)`
  - `h` = height of the tree (recursion stack).

### Example

```text
Input:

      4
     / \
    2   7
   / \ / \
  1  3 6  9

After inversion:

      4
     / \
    7   2
   / \ / \
  9  6 3  1

Output:
Inverted binary tree
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

## 0589 - N-ary Tree Preorder Traversal

- **Problem:** Return the preorder traversal of an N-ary tree.
- **Pattern:** `Tree Traversal` / `Recursion`
- **Recognition:**
  - Each node can have any number of children.
  - Preorder traversal always visits:
    - Root
    - Then each child from left to right.
  - A recursive DFS naturally follows this order.
- **Key Insight:**
  - If the current node is `None`, stop recursion.
  - Visit the current node by adding its value to the result.
  - Recursively traverse each child in order.
  - Continue until all nodes have been visited.

- **Time Complexity:** `O(n)`
  - Every node is visited exactly once.
- **Space Complexity:** `O(h)`
  - `h` = height of the tree (recursion stack).

### Example

```text
Input:

        1
      / | \
     3  2  4
    / \
   5   6

Preorder:
1 → 3 → 5 → 6 → 2 → 4

Output:
[1, 3, 5, 6, 2, 4]
```

## 0590 - N-ary Tree Postorder Traversal

- **Problem:** Return the postorder traversal of an N-ary tree.
- **Pattern:** `Tree Traversal` / `Recursion`
- **Recognition:**
  - Each node may have multiple children.
  - Postorder traversal visits all children before the current node.
  - A recursive DFS naturally processes nodes in this order.
- **Key Insight:**
  - If the current node is `None`, stop recursion.
  - Recursively traverse each child from left to right.
  - After all children have been visited, add the current node's value to the result.
  - Continue until every node has been processed.

- **Time Complexity:** `O(n)`
  - Every node is visited exactly once.
- **Space Complexity:** `O(h)`
  - `h` = height of the tree (recursion stack).

### Example

```text
Input:

        1
      / | \
     3  2  4
    / \
   5   6

Postorder:
5 → 6 → 3 → 2 → 4 → 1

Output:
[5, 6, 3, 2, 4, 1]
```

## 2331 - Evaluate Boolean Binary Tree

- **Problem:** Evaluate a boolean binary tree where:
  - Leaf nodes contain `0` (False) or `1` (True).
  - Internal nodes contain:
    - `2` → OR
    - `3` → AND
- **Pattern:** `Binary Tree` / `Recursion`
- **Recognition:**
  - Each internal node's value depends on the results of its children.
  - Leaf nodes represent the base cases.
  - A post-order traversal naturally evaluates the tree.
- **Key Insight:**
  - If the node is a leaf:
    - `0` → `False`
    - `1` → `True`
  - Otherwise:
    - `2` → evaluate `left OR right`
    - `3` → evaluate `left AND right`
  - Recursively compute child values until the entire expression is evaluated.

- **Time Complexity:** `O(n)`
  - Every node is visited exactly once.
- **Space Complexity:** `O(h)`
  - `h` = height of the tree (recursion stack).

### Example

```text
Input:

      OR
     /  \
   True AND
        / \
    False True

Evaluation:
True OR (False AND True)
= True OR False
= True

Output:
True
```