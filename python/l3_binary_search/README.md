# Binary Search

### Easy

- [0704 - Binary Search](#0704---binary-search)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>


## 0704 - Binary Search

- **Problem:** Given a sorted array and a target value, return the index of the target. If it does not exist, return `-1`.
- **Pattern:** `Binary Search`
- **Recognition:**
  - The array is sorted.
  - Need efficient lookup of a target value.
  - Search space can be halved after each comparison.
- **Key Insight:**
  - Maintain a search window `[low, high]`.
  - Compute the middle index:
    ```text
    mid = (low + high) // 2
    ```
  - If the target is smaller, search the left half.
  - If the target is larger, search the right half.
  - If the target equals `nums[mid]`, return `mid`.
  - If the search window becomes empty, the target is not present.

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 9

mid = 2 -> 3
Search right half

mid = 4 -> 9

Output:
4
```