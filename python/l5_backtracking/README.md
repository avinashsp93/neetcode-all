# Backtracking

### Easy

- [1863 - Sum of All Subset XOR Totals](#1863---sum-of-all-subset-xor-totals)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

## 1863 - Sum of All Subset XOR Totals

- **Problem:** Compute the sum of the XOR totals of every possible subset of an array.
- **Pattern:** `Backtracking` / `DFS`
- **Recognition:**
  - Every element has two choices:
    - Include it in the current subset.
    - Exclude it from the current subset.
  - Need to explore all possible subsets.
- **Key Insight:**
  - Use DFS to recursively build subsets.
  - At each index:
    - Include the current element by XORing it with the running total.
    - Exclude the current element and leave the running total unchanged.
  - When all elements have been processed, return the XOR total for that subset.
  - Sum the results from both recursive branches.

- **Time Complexity:** `O(2ⁿ)`
- **Space Complexity:** `O(n)`
  - Due to the recursion stack.

### Example

```text
Input:
nums = [1, 3]

Subsets:
[]      -> 0
[1]     -> 1
[3]     -> 3
[1,3]   -> 2

Sum:
0 + 1 + 3 + 2 = 6

Output:
6
```