# Sliding Window

### Easy

- [0121 - Best Time to Buy and Sell Stock](#0121---best-time-to-buy-and-sell-stock)
- [0219 - Contains Duplicate II](#0219---contains-duplicate-ii)




<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

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