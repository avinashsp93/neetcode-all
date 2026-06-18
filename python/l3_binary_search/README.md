# Binary Search

### Easy

- [0035 - Search Insert Position](#0035---search-insert-position)
- [0069 - Sqrt(x)](#0069---sqrtx)
- [0367 - Valid Perfect Square](#0367---valid-perfect-square)
- [0374 - Guess Number Higher or Lower](#0374---guess-number-higher-or-lower)
- [0441 - Arranging Coins](#0441---arranging-coins)
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
## 0069 - Sqrt(x)

- **Problem:** Compute and return the integer square root of `x`, rounded down to the nearest integer.
- **Pattern:** `Binary Search`
- **Recognition:**
  - Need the largest integer whose square does not exceed `x`.
  - The search space is sorted from `1` to `x`.
  - Binary search efficiently finds this boundary.
- **Key Insight:**
  - Search for the largest value `mid` satisfying:
    
    
    
  - If `mid²` is too large, search left.
  - If `mid²` is too small, search right.
  - If an exact square root is found, return it.
  - When the search ends, `high` points to the integer square root.

- **Time Complexity:** `O(log x)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
x = 8

mid = 4 -> 16 > 8
mid = 2 -> 4 < 8
mid = 3 -> 9 > 8

Largest integer with square ≤ 8:
2

Output:
2
```


## 0367 - Valid Perfect Square

- **Problem:** Determine whether a positive integer is a perfect square without using built-in square root functions.
- **Pattern:** `Binary Search`
- **Recognition:**
  - Need to find whether an integer `x` exists such that:
    
    
    
  - The search space is sorted (`1` to `num`).
  - Binary search can efficiently locate the square root candidate.
- **Key Insight:**
  - Search within the range `[1, num]`.
  - For each midpoint:
    - Compute `mid²`.
    - If `mid² > num`, search left.
    - If `mid² < num`, search right.
    - If `mid² == num`, `num` is a perfect square.
  - If the search ends without a match, return `False`.

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
num = 16

mid = 8  -> 64  > 16
mid = 4  -> 16 == 16

Output:
True
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

## 0441 - Arranging Coins

- **Problem:** Given `n` coins, build a staircase where the `i-th` row contains exactly `i` coins. Return the number of complete rows that can be formed.
- **Pattern:** `Math` / `Binary Search`
- **Recognition:**
  - Rows require:
    ```text
    1 + 2 + 3 + ... + k
    ```
    coins.
  - Need the largest `k` such that:
    ```text
    k(k + 1)/2 <= n
    ```
  - Can be solved using simulation, binary search, or the quadratic formula.

### Solution 1: Simulation

- Build rows one at a time.
- Subtract the required coins for each row.
- Stop when there are not enough coins for the next row.

- **Time Complexity:** `O(√n)`
- **Space Complexity:** `O(1)`

### Solution 2: Binary Search

- Use the formula for the sum of the first `k` natural numbers:
  ```text
  S(k) = k(k + 1)/2
  ```
- Search for the largest `k` satisfying:
  ```text
  k(k + 1)/2 <= n
  ```
- If the triangular number is too large, search left.
- Otherwise, search right.
- After the search, `high` stores the answer.

- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

### Solution 3: Math Formula

- Solve:
  ```text
  k(k + 1)/2 = n
  ```
- Using the quadratic formula:

  

- The answer is the integer floor of the expression.

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
n = 8

Rows:
1 coin  -> complete
2 coins -> complete
3 coins -> complete

Coins used:
1 + 2 + 3 = 6

Remaining:
2

Cannot complete the 4th row.

Output:
3
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