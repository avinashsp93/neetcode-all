# Sliding Window

### Easy

- [0121 - Best Time to Buy and Sell Stock](#0121---best-time-to-buy-and-sell-stock)
- [0219 - Contains Duplicate II](#0219---contains-duplicate-ii)
- [1652 - Defuse the Bomb](#1652---defuse-the-bomb)
- [1984 - Minimum Difference Between Highest and Lowest of K Scores](#1984---minimum-difference-between-highest-and-lowest-of-k-scores)
- [2379 - Minimum Recolors to Get K Consecutive Black Blocks](#2379---minimum-recolors-to-get-k-consecutive-black-blocks)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

## 0121 - Best Time to Buy and Sell Stock

- **Problem:** Given the price of a stock on each day, determine the maximum profit that can be achieved by buying once and selling once.
- **Pattern:** `Two Pointers`
- **Recognition:**
  - Buy must occur before sell.
  - Need to track the lowest buying price seen so far.
  - A single pass is sufficient to compute the maximum profit.
- **Key Insight:**
  - Use two pointers:
    - `left` → candidate buying day (lowest price so far)
    - `right` → current selling day
  - If `prices[right]` is lower than `prices[left]`, move `left` to `right` since it is a better buying opportunity.
  - Otherwise, compute the profit and update the maximum.
  - Continue until all days have been processed.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
prices = [7, 1, 5, 3, 6, 4]

Buy:
Day 2 (price = 1)

Sell:
Day 5 (price = 6)

Profit:
6 - 1 = 5

Output:
5
```

## 0219 - Contains Duplicate II

- **Problem:** Determine whether there exist two equal values in the array whose indices differ by at most `k`.
- **Pattern:** `Sliding Window` / `Hash Set`
- **Recognition:**
  - Need to check duplicates within a limited distance.
  - Only the last `k` elements are relevant for each position.
  - A hash set provides `O(1)` duplicate lookups.
- **Key Insight:**
  - Maintain a sliding window of at most `k` elements using a set.
  - As the right pointer expands:
    - Remove elements that fall outside the window.
    - Check if the current value already exists in the set.
  - If it does, a valid duplicate has been found.
  - Otherwise, add the current value to the window.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(min(n, k))`

### Example

```text
Input:
nums = [1, 2, 3, 1]
k = 3

Window:
[1] -> {1}
[1,2] -> {1,2}
[1,2,3] -> {1,2,3}

Next value:
1 already exists in the window.

Output:
True
```

## 1652 - Defuse the Bomb

- **Problem:** Replace each element with the sum of the next `k` elements (or previous `|k|` elements if `k` is negative). If `k = 0`, replace every element with `0`.
- **Pattern:** `Sliding Window` / `Circular Array`
- **Recognition:**
  - Need sums of consecutive elements.
  - The array wraps around, making it circular.
  - A sliding window avoids recomputing each sum from scratch.
- **Key Insight:**
  - Handle the special case `k = 0` by returning an array of zeros.
  - Compute the initial window sum:
    - Next `k` elements if `k > 0`
    - Previous `|k|` elements if `k < 0`
  - Slide the window one position at a time:
    - Remove the element leaving the window.
    - Add the new element entering the window.
  - Use modulo (`% n`) to wrap indices around the circular array.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
  - For the output array.

### Example

```text
Input:
code = [5, 7, 1, 4]
k = 3

Window sums:
5 -> 7 + 1 + 4 = 12
7 -> 1 + 4 + 5 = 10
1 -> 4 + 5 + 7 = 16
4 -> 5 + 7 + 1 = 13

Output:
[12, 10, 16, 13]
```

## 1984 - Minimum Difference Between Highest and Lowest of K Scores

- **Problem:** Select `k` scores such that the difference between the highest and lowest score is minimized.
- **Pattern:** `Sorting` / `Sliding Window`
- **Recognition:**
  - Need the minimum range among groups of `k` elements.
  - Sorting places close values together.
  - A fixed-size sliding window can evaluate every possible group efficiently.
- **Key Insight:**
  - Sort the array.
  - If `k = 1`, the difference is `0`.
  - Slide a window of size `k` across the sorted array.
  - For each window, compute:
    ```text
    sorted_nums[right] - sorted_nums[left]
    ```
  - Track the minimum difference across all windows.

- **Time Complexity:** `O(n log n)`
  - Sorting dominates the runtime.
- **Space Complexity:** `O(n)`
  - Due to creating the sorted array.

### Example

```text
Input:
nums = [9, 4, 1, 7]
k = 2

Sorted:
[1, 4, 7, 9]

Window differences:
4 - 1 = 3
7 - 4 = 3
9 - 7 = 2

Minimum difference:
2

Output:
2
```

## 2379 - Minimum Recolors to Get K Consecutive Black Blocks

- **Problem:** Find the minimum number of white blocks that must be recolored to obtain `k` consecutive black blocks.
- **Pattern:** `Sliding Window`
- **Recognition:**
  - Need to evaluate every consecutive substring of length `k`.
  - The number of white blocks in each window determines the recolors needed.
  - A fixed-size sliding window updates the count efficiently.
- **Key Insight:**
  - Initialize a window of size `k` and count the number of `'W'` blocks.
  - Slide the window one position at a time:
    - Add the new block entering the window.
    - Remove the block leaving the window.
  - Track the minimum number of white blocks across all windows.
  - That minimum is the answer.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
  - The frequency map stores only `'B'` and `'W'`.

### Example

```text
Input:
blocks = "WBBWWBBWBW"
k = 3

Windows:
WBB -> 1 white
BBW -> 1 white
BWW -> 2 whites
...
WBB -> 1 white

Minimum whites:
1

Output:
1
```
