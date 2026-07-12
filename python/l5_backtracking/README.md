# Backtracking

### Easy

- [1863 - Sum of All Subset XOR Totals](#1863---sum-of-all-subset-xor-totals)

### Medium

- [0039 - Combination Sum I](#0039---combination-sum-i)
- [0040 - Combination Sum II](#0040---combination-sum-ii)
- [0078 - Subsets I](#0078---subsets-i)
- [0090 - Subsets II](#0090---subsets-ii)

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

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  MEDIUM PROBLEMS
</h2>

## 0039 - Combination Sum I

- **Problem:** Find all unique combinations of candidate numbers that sum to a target. Each candidate may be used an unlimited number of times.
- **Pattern:** `Backtracking` / `DFS`
- **Recognition:**
  - Need to generate all valid combinations.
  - Each candidate has two choices:
    - Skip it and move to the next candidate.
    - Include it and remain at the same index (since reuse is allowed).
  - The search stops when the target is reached or exceeded.
- **Key Insight:**
  - Use DFS with three pieces of state:
    - Current candidate index.
    - Current combination.
    - Remaining target.
  - At each step:
    - **Skip** the current candidate and recurse to the next index.
    - **Take** the current candidate, subtract its value from the remaining target, and recurse at the same index.
  - If the remaining target becomes `0`, a valid combination has been found.
  - If the remaining target becomes negative or all candidates have been considered, stop exploring that branch.

- **Time Complexity:** `O(2^t)` _(output-dependent)_
  - The number of valid combinations grows exponentially with the target and candidate values.
- **Space Complexity:** `O(t)`
  - `t` = maximum recursion depth (bounded by the target in the worst case, excluding the output).

### Example

```text
Input:
candidates = [2, 3, 6, 7]
target = 7

Choices:
Take 2 -> [2,2,3]
Take 7 -> [7]

Output:
[[2,2,3], [7]]
```

## 0040 - Combination Sum II

- **Problem:** Find all unique combinations of candidate numbers that sum to a target. Each candidate may be used **at most once**.
- **Pattern:** `Backtracking` / `DFS`
- **Recognition:**
  - Need to generate combinations while avoiding duplicates.
  - Duplicate candidate values can produce identical combinations.
  - Sorting groups duplicates together, making them easy to skip.
- **Key Insight:**
  - Sort the candidates first.
  - Use DFS with:
    - Current index.
    - Current combination.
    - Remaining target.
  - At each index:
    - **Skip branch:** Skip all consecutive duplicate values before moving to the next distinct candidate.
    - **Take branch:** Include the current candidate, reduce the remaining target, and recurse to the **next index** since each element can only be used once.
  - If the remaining target becomes `0`, record the current combination.
  - Stop exploring when the remaining target becomes negative or all candidates have been considered.

- **Time Complexity:** `O(2ⁿ)` _(output-dependent)_
- **Space Complexity:** `O(n)`
  - Due to the recursion stack (excluding the output).

### Example

```text
Input:
candidates = [10,1,2,7,6,1,5]
target = 8

Sorted:
[1,1,2,5,6,7,10]

Output:
[
  [1,1,6],
  [1,2,5],
  [1,7],
  [2,6]
]
```

## 0078 - Subsets I

- **Problem:** Return all possible subsets of a given array of unique integers.
- **Pattern:** `Backtracking` / `DFS`
- **Recognition:**
  - Every element has two possible decisions:
    - Include the element in the subset.
    - Exclude the element from the subset.
  - Exploring both decisions creates all possible combinations.
- **Key Insight:**
  - Use DFS with the current index and subset state.
  - At each index:
    - **Skip branch:** Move to the next element without adding the current value.
    - **Take branch:** Add the current value and move to the next element.
  - When all elements have been processed, add the current subset to the result.
  - Use copies when branching to avoid modifying previous subsets.

- **Time Complexity:** `O(n · 2ⁿ)`
  - There are `2ⁿ` possible subsets, each requiring up to `O(n)` to store.
- **Space Complexity:** `O(n)`
  - Due to recursion depth (excluding output).

### Example

```text
Input:
nums = [1, 2]

Decisions:

1 excluded, 2 excluded -> []
1 excluded, 2 included -> [2]
1 included, 2 excluded -> [1]
1 included, 2 included -> [1,2]

Output:
[[], [2], [1], [1,2]]
```

## 0090 - Subsets II

- **Problem:** Return all possible subsets of an array that may contain duplicates. The result must not contain duplicate subsets.
- **Pattern:** `Backtracking` / `DFS`
- **Recognition:**
  - Similar to generating subsets, but duplicate values can create duplicate combinations.
  - Need to avoid exploring identical decision branches.
  - Sorting helps group duplicate values together.
- **Key Insight:**
  - Sort the array so duplicate values are adjacent.
  - At each index:
    - **Skip branch:** Skip all duplicate values together and move to the next unique value.
    - **Take branch:** Include the current value and continue exploring.
  - This ensures identical subsets are not generated multiple times.
  - When all elements are processed, add the current subset to the result.

- **Time Complexity:** `O(n · 2ⁿ)`
  - In the worst case, all subsets may still need to be generated.
- **Space Complexity:** `O(n)`
  - Due to recursion depth (excluding output).

### Example

```text
Input:
nums = [1, 2, 2]

Sorted:
[1, 2, 2]

Subsets:
[]
[1]
[2]
[1,2]
[2,2]
[1,2,2]

Output:
[[], [1], [2], [1,2], [2,2], [1,2,2]]
```
