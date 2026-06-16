# Binary Search

### Easy

- [0035 - Search Insert Position](#0035---search-insert-position)
- [0374 - Guess Number Higher or Lower](#0374---guess-number-higher-or-lower)
- [0704 - Binary Search](#0704---binary-search)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

## 0035 - Search Insert Position

- **Problem:** Given a sorted array and a target value, return its index if found. Otherwise, return the index where it should be inserted to maintain sorted order.
- **Pattern:** `Binary Search`
- **Recognition:**
  - The array is sorted.
  - Need either the exact position or the correct insertion point.
  - Binary search naturally converges to the insertion index.
- **Key Insight:**
  - Perform a standard binary search.
  - If the target is found, return its index.
  - If the target is not found, the search ends with:
    ```text
    low = insertion position
    ```
  - Return `low`, which represents the first index where the target can be inserted while preserving sorted order.

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [1, 3, 5, 6]
target = 2

Binary Search:
2 < 5 -> search left
2 < 3 -> search left

Search ends:
low = 1

Output:
1
```


## 0374 - Guess Number Higher or Lower

- **Problem:** Guess a hidden number between `1` and `n` using the provided `guess()` API.
- **Pattern:** `Binary Search`
- **Recognition:**
  - Search space is a sorted range of numbers.
  - Feedback indicates whether the guess is too high or too low.
  - The search interval can be halved after each guess.
- **Key Insight:**
  - Maintain a search range `[low, high]`.
  - Guess the middle number.
  - Use the API response:
    - `-1` → guess is too high, search left half.
    - `1` → guess is too low, search right half.
    - `0` → correct answer found.
  - Repeat until the number is found.

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
n = 10
picked = 6

Guess 5 -> too low
Guess 8 -> too high
Guess 6 -> correct

Output:
6
```

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