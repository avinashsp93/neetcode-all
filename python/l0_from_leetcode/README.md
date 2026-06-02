# From LeetCode

This directory contains solutions to various problems from LeetCode, categorized by difficulty level. Each problem includes a brief description, the pattern it follows, recognition tips, key insights for solving it, and an analysis of time and space complexity.

### Easy

- [0028 - Find the Index of the First Occurrence in a String](#0028---find-the-index-of-the-first-occurrence-in-a-string)
- [0029 - Divide Two Integers](#0029---divide-two-integers)
- [0066 - Plus One](#0066---plus-one)
- [0067 - Add Binary](#0067---add-binary)
- [0070 - Climbing Stairs](#0070---climbing-stairs)
- [0136 - Single Number](#0136---single-number)
- [0171 - Excel Sheet Column Number](#0171---excel-sheet-column-number)
- [0268 - Missing Number](#0268---missing-number)
- [0278 - First Bad Version](#0278---first-bad-version)
- [0383 - Ransom Note](#0383---ransom-note)
- [0389 - Find the Difference](#0389---find-the-difference)
- [0412 - Fizz Buzz](#0412---fizz-buzz)
- [0482 - License Key Formatting](#0482---license-key-formatting)
- [0509 - Fibonacci Number](#0509---fibonacci-number)
- [1572 - Matrix Diagonal Sum](#1572---matrix-diagonal-sum)
- [1137 - N-th Tribonacci Number](#1137---n-th-tribonacci-number)
- [1160 - Find Words That Can Be Formed by Characters (Leetcode 1160)](#1160---find-words-that-can-be-formed-by-characters-leetcode-1160)
- [1588 - Sum of All Odd Length Subarrays](#1588---sum-of-all-odd-length-subarrays)
- [1886 - Determine Whether Matrix Can Be Obtained By Rotation](#1886---determine-whether-matrix-can-be-obtained-by-rotation)
- [2133 - Check if Every Row and Column Contains All Numbers](#2133---check-if-every-row-and-column-contains-all-numbers)
- [Rearrange Characters to Form Target String (Leetcode 2287)](#rearrange-characters-to-form-target-string-leetcode-2287)
- [2319 - Check if Matrix is X-Matrix](#2319---check-if-matrix-is-x-matrix)
- [3158 - Find the XOR of Numbers Which Appear Twice](#3158---find-the-xor-of-numbers-which-appear-twice)
- [0036 - Valid Sudoku](#0036---valid-sudoku)
- [0054 - Rotate Image](#0054---rotate-image)
- [0054 - Spiral Matrix](#0054---spiral-matrix)
- [0059 - Spiral Matrix II](#0059---spiral-matrix-ii)
- [0287 - Find the Duplicate Number](#0287---find-the-duplicate-number)

### Medium

- [0036 - Valid Sudoku](#0036---valid-sudoku)
- [0048 - Rotate Image](#0048---rotate-image)
- [0054 - Spiral Matrix](#0054---spiral-matrix)
- [0059 - Spiral Matrix II](#0059---spiral-matrix-ii)
- [0287 - Find the Duplicate Number](#0287---find-the-duplicate-number)

## 0028 - Find the Index of the First Occurrence in a String

- **Problem:** Return the starting index of the first occurrence of `needle` in `haystack`.  
  Return `-1` if `needle` does not exist.
- **Pattern:** `Sliding Window` / `Brute Force String Matching`
- **Recognition:**
  - Need substring search
  - Compare a smaller pattern against every possible starting position
  - Sequential character matching problem
- **Key Insight:**
  - Iterate through all valid starting indices in `haystack`
  - For each position:
    - compare characters one-by-one with `needle`
  - First complete match returns starting index
- **Time Complexity:** `O((n - m + 1) * m)`
  - worst-case `O(nm)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
haystack = "sadbutsad"
needle = "sad"

Check:
"sad" ✅

First occurrence index:
0

Output:
0

Input:
haystack = "leetcode"
needle = "leeto"

Mismatch occurs

Output:
-1
```

## 0029 - Divide Two Integers

- **Problem:** Divide two integers without using:
  - multiplication
  - division
  - modulo  
    Return the truncated quotient.
- **Pattern:** `Math` / `Repeated Subtraction`
- **Recognition:**
  - Restricted arithmetic operations
  - Need manual simulation of division
  - Quotient represents repeated removal of divisor
- **Key Insight:**
  - Division can be simulated through repeated subtraction:

  :contentReference[oaicite:0]{index=0}
  - Determine sign separately:
    - same signs → positive quotient
    - different signs → negative quotient
  - Count how many times divisor can be subtracted before crossing zero

- **Time Complexity:** `O(|quotient|)`
  - very slow for large inputs
- **Space Complexity:** `O(1)`

### Example

```text
Input:
dividend = 10
divisor = 3

Process:
10 - 3 = 7
7 - 3 = 4
4 - 3 = 1

Subtracted 3 times

Output:
3
Input:
dividend = 7
divisor = -3

Quotient:
-2
```

## 0066 - Plus One

- **Problem:** Given a large integer represented as an array of digits, increment the integer by one and return the resulting array.
- **Pattern:** `Simulation` / `Carry Propagation`
- **Recognition:**
  - Digit-by-digit arithmetic
  - Right-to-left traversal
  - Carry handling similar to elementary addition
- **Key Insight:**
  - Start with carry = `1` because we are adding one
  - Traverse digits from right to left:
    - digit + carry
    - if result becomes `10`:
      - store `0`
      - propagate carry
    - otherwise:
      - carry becomes `0`
  - If carry remains after traversal, prepend `1`
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
  - due to result array

### Example

```text
Input:
digits = [1,2,9]

Process:
9 + 1 = 10 → write 0, carry 1
2 + 1 = 3 → carry cleared
1 remains unchanged

Output:
[1,3,0]

Input:
digits = [9,9,9]

Process:
999 + 1 = 1000

Output:
[1,0,0,0]
```

## 0067 - Add Binary

- **Problem:** Given two binary strings `a` and `b`, return their sum as a binary string.
- **Pattern:** `Bit Manipulation` / `Simulation`
- **Recognition:**
  - Recognize binary addition rules by plotting out truth table
  - Binary addition
  - Right-to-left digit traversal
  - Carry propagation between positions
- **Key Insight:**
  - Simulate binary addition from least significant bit
  - Use:

  sum = a XOR b XOR carry

  for resulting bit

  and:

  carry = (a AND b) OR ((a XOR b) AND carry)

  for carry propagation

- **Time Complexity:** `O(max(n,m))`
- **Space Complexity:** `O(max(n,m))`

### Example

```text
Input:
a = "11"
b = "1"

Process:
1 + 1 = 10
1 + carry = 10

Output:
"100"

Input:
a = "1010"
b = "1011"

Binary Addition:
1010
1011
----
10101

Output:
"10101"
```

## 0070 - Climbing Stairs

- **Problem:** Given `n` stairs, where you can climb either `1` or `2` steps at a time, return the number of distinct ways to reach the top.
- **Pattern:** `Dynamic Programming` / `Memoized Recursion`
- **Recognition:**
  - Count total ways to reach a target
  - Current state depends on smaller subproblems
  - Fibonacci-like structure
- **Key Insight:**
  - To write the code, use the following rule
    - Check
    - Compute
    - Cache
    - Return
  - To reach stair `n`:
    - come from `n - 1` with a 1-step move
    - come from `n - 2` with a 2-step move

  Recurrence:

  f(n)=f(n−1)+f(n−2)
  - Store previously computed results in a memo table to avoid recomputation

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
n = 4

Ways to reach 4:

From stair 3:
f(3)

From stair 2:
f(2)

f(4) = f(3) + f(2)
     = 3 + 2
     = 5

Output:
5
```

## 0136 - Single Number

- **Problem:** Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
- **Pattern:** `Bit Manipulation`
- **Recognition:**
  - Each element appears twice except for one
  - XOR operation can be used to cancel out pairs
- **Key Insight:**
  - XOR all elements in the array
  - Since XOR of a number with itself is 0, and XOR is commutative and associative, the result will be the single number that does not have a pair
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [2,2,1]

Output:
1

Input:
nums = [4,1,2,1,2]

Output:
4
```

## 0171 - Excel Sheet Column Number

- **Problem:** Given a string representing an Excel column title, return its corresponding column number.
- **Pattern:** `Math` / `Base Conversion`
- **Recognition:**
  - Recognize the pattern as a base-26 number system
  - Each character represents a digit in base-26
  - The rightmost character has the lowest weight
- **Key Insight:**
  - Convert each character to its numeric value (A=1, B=2, ..., Z=26)
  - Use the formula for base conversion:
    result = result \* 26 + current_value
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
columnTitle = "A"

Output:
1

Input:
columnTitle = "AB"

Output:
27
```

## 0268 - Missing Number

- **Problem:** Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.
- **Pattern:** `Math` / `Bit Manipulation`
- **Recognition:**
  - Array of distinct numbers in a known range
  - Need to find the one missing number
  - Can use mathematical properties or bit manipulation
- **Key Insight:**
  - Use the formula for the sum of an arithmetic sequence:
    expected_sum = n \* (n + 1) / 2
  - Calculate the actual sum of the array
  - The difference is the missing number
  - Bit manipulation approach: XOR all numbers in the array with all numbers in the range [0, n]
    - Since XOR of a number with itself is 0, and XOR is commutative and associative, the result will be the missing number
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [3,0,1]

Output:
2

Input:
nums = [0,1]

Output:
2
```

## 0278 - First Bad Version

- **Problem:** Given versions `1` to `n`, where all versions after the first bad version are also bad, find the first bad version using the provided `isBadVersion()` API.
- **Pattern:** `Binary Search on Answer`
- **Recognition:**
  - Search space is sorted by a boolean condition
  - Once a version becomes bad, all subsequent versions are bad
  - Looking for the **first occurrence** that satisfies a condition
- **Key Insight:**
  - The versions form a monotonic sequence:

  ```text
  F F F F T T T T
          ^
      first bad
  ```

  - If mid version is bad → set the bad version to mid and continue searching left half
  - If mid version is good → search right half

  - Time Complexity: O(log n)
  - Space Complexity: O(1)

## 0383 - Ransom Note

- **Problem:** Determine if a `ransomNote` can be constructed from letters in `magazine`, where each letter can only be used once.
- **Pattern:** `Hash Map / Frequency Counting`
- **Recognition:**
  - Need to track availability of characters
  - Repeated consumption of limited resources
  - Greedy character usage with constraints
- **Key Insight:**
  - Build frequency map of `magazine`
  - For each character in `ransomNote`:
    - check availability in map
    - decrement count if usable
    - fail immediately if unavailable
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(1)` (bounded alphabet size)

### Example

```text
Input:
ransomNote = "aa"
magazine = "ab"

Process:
a → available (1 → 0)
a → not available → fail

Output:
False
```

## 0389 - Find the Difference

- **Problem:** Given strings `s` and `t` where `t` is generated by shuffling `s` and adding one extra character, return the extra character.
- **Pattern:** `Bit Manipulation` / `Hash Map`
- **Recognition:**
  - Two nearly identical collections
  - One extra element needs detection
  - XOR often fits:
    - pair cancellation
    - missing/extra element problems
- **Key Insight:**
  - XOR property:

  a ^ a = 0

  and:

  a ^ 0 = a
  - All matching characters cancel out
  - Remaining XOR value corresponds to the extra character

- **Time Complexity:** `O(n)`
- **Space Complexity:**
  - Hash map approach: `O(1)`
  - XOR approach: `O(1)`

### Example

```text
Input:
s = "abcd"
t = "abcde"

XOR Process:
a ^ a = 0
b ^ b = 0
c ^ c = 0
d ^ d = 0

Remaining:
e

Output:
"e"
```

## 0412 - Fizz Buzz

- **Problem:** Generate a list from `1` to `n` where:
  - multiples of 3 → `"Fizz"`
  - multiples of 5 → `"Buzz"`
  - multiples of both → `"FizzBuzz"`
  - otherwise → number as string
- **Pattern:** `Simulation` / `Conditional Logic`
- **Recognition:**
  - Simple iteration with rule-based replacements
  - Divisibility conditions drive output transformation
  - Order of checks matters (combined case first)
- **Key Insight:**
  - Check the most restrictive condition first:
    - divisible by both 3 and 5 (i.e., divisible by 15)
    - This ensures that the combined case is handled before the individual cases

    i % 3 == 0 and i % 5 == 0

  - Then handle single conditions:
    - divisible by 3
    - divisible by 5

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
n = 5

Output:
["1","2","Fizz","4","Buzz"]
```

## 0482 - License Key Formatting

- **Problem:** Reformat a license key string by:
  - removing existing dashes
  - converting to uppercase
  - regrouping characters in groups of size `k` from right to left
- **Pattern:** `String Manipulation` / `Greedy Formatting`
- **Recognition:**
  - formatting requirement, not transformation logic
  - grouping from the end is key (right-aligned chunks)
  - dash placement depends on reversed traversal
- **Key Insight:**
  - Remove all `-` and normalize case first
  - Traverse string **backwards**
  - Build result while inserting `-` every `k` characters
  - Reverse final string to restore correct order
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
s = "2-5g-3-J", k = 2

Cleaned:
25G3J

Reverse build:
J3-G5-2

Final:
2-5G-3J
```

## 0509 - Fibonacci Number

- **Problem:** Given `n`, return the `n`th Fibonacci number.
- **Pattern:** `Dynamic Programming` / `Memoized Recursion`
- **Recognition:**
  - Recursive definition with overlapping subproblems
  - Same values are recomputed multiple times in naive recursion
  - Natural fit for memoization
- **Key Insight:**
  - Fibonacci follows the recurrence:
  - To write the code, use the following rule
    - Check
    - Compute
    - Cache
    - Return

  f(n)=f(n−1)+f(n−2)
  - Cache previously computed results in a memo table
  - Each Fibonacci value is computed exactly once

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
n = 5

F(5)
= F(4) + F(3)
= 3 + 2
= 5

Output:
5
```

## 1572 - Matrix Diagonal Sum

- **Problem:** Return the sum of the primary and secondary diagonals of a square matrix.  
  Avoid double-counting the center element when `n` is odd.
- **Pattern:** `Matrix Traversal`
- **Recognition:**
  - Square matrix (`n x n`)
  - Need both diagonals:
    - primary: `mat[i][i]`
    - secondary: `mat[i][n-1-i]`
  - Overlap occurs at center when `n` is odd
- **Key Insight:**
  - Both diagonals can be computed in a single loop
  - Use index relationship:

  :contentReference[oaicite:0]{index=0}
  - If `i == j`, it's the center element → add only once

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
mat = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Primary diagonal: 1 + 5 + 9
Secondary diagonal: 3 + 5 + 7

Center (5) counted once

Output:
25
```

## 1137 - N-th Tribonacci Number

- **Problem:** Given `n`, return the `n`th Tribonacci number, where each number is the sum of the previous three numbers.
- **Pattern:** `Dynamic Programming` / `Memoized Recursion`
- **Recognition:**
  - Recursive sequence with overlapping subproblems
  - Each state depends on the previous three states
  - Naive recursion would recompute the same values many times
- **Key Insight:**
  - To write the code, use the following rule
    - Check
    - Compute
    - Cache
    - Return
  - Tribonacci follows the recurrence:

    T(n) = T(n-1) + T(n-2) + T(n-3)

  - Store computed values in a memo table
  - Each Tribonacci number is calculated only once

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
n = 4

T(4)
= T(3) + T(2) + T(1)
= 2 + 1 + 1
= 4

Output:
4
```

## 1160 - Find Words That Can Be Formed by Characters (Leetcode 1160)

- **Problem:** Given a list of words and a string `chars`, return the total length of words that can be formed using letters from `chars` (each letter can be used only as many times as it appears in `chars`).
- **Pattern:** `Hash Map / Frequency Counting`
- **Recognition:**
  - Each word must be validated against a fixed character supply
  - Repeated constraint checking per word
  - Frequency comparison between two multisets
- **Key Insight:**
  - Build frequency map of available characters:

    chars frequency ≥ word frequency

  - For each word:
    - build its frequency map
    - ensure no character exceeds available count
    - if valid, add word length to result

- **Time Complexity:** `O(N * K)`
  - N = number of words
  - K = average word length
- **Space Complexity:** `O(1)`
  - bounded alphabet size (26 lowercase letters)

### Example

```text
Input:
words = ["cat","bt","hat","tree"]
chars = "atach"

Valid words:
- "cat" ✓
- "bt" ✗
- "hat" ✓
- "tree" ✗

Output:
6
```

## 1588 - Sum of All Odd Length Subarrays

- **Problem:** Find the sum of all subarrays of `arr` that have odd length.
- **Pattern:** `Prefix Sum (Implicit)` / `Brute Force Enumeration`
- **Recognition:**
  - Subarray-based problem
  - Need to consider all contiguous segments
  - Condition depends on subarray length parity (odd length only)
- **Key Insight:**
  - Iterate over all subarray start indices
  - Expand end index while maintaining running sum
  - Include subarray sum only when its length is odd

  Length condition:
  (j - i) % 2 == 0
  - Running sum avoids recomputing from scratch each time

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
arr = [1,4,2,5,3]

Odd subarrays:
[1], [4], [2], [5], [3]
[1,4,2], [4,2,5], [2,5,3]
[1,4,2,5,3]

Sum:
= 58
```

## 1886 - Determine Whether Matrix Can Be Obtained By Rotation

- **Problem:** Determine whether `target` can be obtained by rotating `mat` by:
  - `0°`
  - `90°`
  - `180°`
  - `270°`
- **Pattern:** `Matrix Transformation` / `Simulation`
- **Recognition:**
  - Rotate 90° clockwise: Flip along horizontal axis + Flip along main diagonal
  - Rotate 180°: Flip along horizontal axis + Flip along vertical axis
  - Rotate 270°: Flip along horizontal axis + Flip along anti-diagonal
  - Common operation is flipping along horizontal axis.
- **Key Insight:**
  - A square matrix has only four unique rotation states:
  - Key things while flipping along horizontal axis:
    - `mat[i][j]` becomes `mat[n-1-i][j]` and i goes from 0 to n//2
  - Key things while flipping along vertical axis:
    - `mat[i][j]` becomes `mat[i][n-1-j]` and j goes from 0 to n//2
  - Key things while flipping along main diagonal:
    - `mat[i][j]` becomes `mat[j][i]` and i goes from 0 to n and j goes from i+1 to n (exclude diagonal)
  - Key things while flipping along anti-diagonal:
    - `mat[i][j]` becomes `mat[n-1-j][n-1-i]` and i goes from 0 to n-1 and j goes from 0 to n-i-1 (exclude diagonal)

  ```text
  0°, 90°, 180°, 270°
  ```

## 2133 - Check if Every Row and Column Contains All Numbers

- **Problem:** Given an `n x n` matrix, check whether every row and every column contains all numbers from `1` to `n` exactly once.
- **Pattern:** `Hash Set` / `Matrix Validation`
- **Recognition:**
  - Each row and column must be a permutation of `[1..n]`
  - Requires uniqueness check across both dimensions
  - Duplicate detection is the core requirement
- **Key Insight:**
  - For each index `i`, validate:
    - row `i`
    - column `i`
  - Use sets to ensure no duplicates appear
  - Any repetition immediately invalidates the matrix
  - Can be written in a single loop by checking both row and column simultaneously
- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
matrix = [
  [1,2,3],
  [3,1,2],
  [2,3,1]
]

Row-wise valid:
[1,2,3], [3,1,2], [2,3,1]

Column-wise valid:
[1,3,2], [2,1,3], [3,2,1]

Output:
True
```

## Rearrange Characters to Form Target String (Leetcode 2287)

- **Problem:** Given strings `s` and `target`, return the maximum number of copies of `target` that can be formed using characters from `s`.
- **Pattern:** `Hash Map / Frequency Counting`
- **Recognition:**
  - Need to form repeated copies of a fixed pattern
  - Resource allocation problem with limited supply
  - Bottleneck determined by the rarest required character
- **Key Insight:**
  - Build frequency map of `s` and `target`
  - For each character in `target`, compute how many full copies it allows:

    minimum frequency ratio across required characters

  - The limiting character determines the final answer

- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(1)`
  - bounded alphabet size

### Example

```text
Input:
s = "ilovecodingonleetcode"
target = "code"

Counts:
c: 2/1 = 2
o: 3/1 = 3
d: 1/1 = 1
e: 3/1 = 3

Bottleneck = 1

Output:
1
```

## 2319 - Check if Matrix is X-Matrix

- **Problem:** Determine whether a square matrix is an X-Matrix:
  - All elements on both diagonals must be non-zero
  - All other elements must be zero
- **Pattern:** `Matrix Traversal` / `Index Condition Checking`
- **Recognition:**
  - Position-based constraints (not value-based structure)
  - Two special index conditions define valid cells
  - Everything depends on diagonal relationships
- **Key Insight:**
  - A cell belongs to the X-shape if:
    i == j or i + j == n - 1
  - If on diagonal → must be non-zero
  - If off diagonal → must be zero

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
grid = [
  [2,0,3],
  [0,5,0],
  [4,0,6]
]

Diagonals:
2, 5, 6 and 3, 5, 4 → valid non-zero

Off-diagonals:
all 0 → valid

Output:
True
```

## 3158 - Find the XOR of Numbers Which Appear Twice

- **Problem:** Return the XOR of all numbers that appear exactly twice in the array.
- **Pattern:** `Bit Manipulation` / `Hash Set`
- **Recognition:**
  - Need duplicate detection
  - XOR cancellation properties are useful
  - Elements appearing once should cancel out
- **Key Insight:**
  - XOR all unique elements
  - XOR all original elements
  - Numbers appearing once cancel completely
  - Numbers appearing twice contribute one remaining occurrence to the final XOR

  Core XOR property:

  a ^ a = 0
  OR
  a ^ a ^ a = a

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
nums = [1,2,1,3]

Unique Set:
{1,2,3}

XOR unique:
1 ^ 2 ^ 3

XOR all nums:
1 ^ 2 ^ 1 ^ 3

Cancellation:
2 and 3 cancel
Remaining:
1

Output:
1
```

## 0036 - Valid Sudoku

- **Problem:** Determine if a partially filled Sudoku board is valid according to Sudoku rules:
  - each row contains unique digits `1-9`
  - each column contains unique digits `1-9`
  - each `3x3` sub-box contains unique digits `1-9`
- **Pattern:** `Hash Set`
- **Recognition:**
  - Need duplicate detection across multiple dimensions
  - Fast membership checking required
  - Grid validation with uniqueness constraints
- **Key Insight:**
  - Use sets to track seen digits for:
    - rows
    - columns
    - `3x3` boxes
  - Ignore `"."` cells since they are empty
  - Any repeated digit immediately invalidates the board
  - Box starting index are 0, 3, 6 for both row and column
  - Nested loops to get the box starting indices and nested loop to iterate through the box cells.

  ```python

  ```

- **Time Complexity:** `O(1)`
  - fixed `9x9` board size
- **Space Complexity:** `O(1)`

### Example

```text
Row Check:
5 3 . . 7 . . . .

Seen:
{5,3,7}

No duplicates → valid

3x3 Box:
5 3 .
6 . .
. 9 8

Seen:
{5,3,6,9,8}

No duplicates → valid
```

## 0054 - Rotate Image

- **Problem:** Rotate an `n x n` matrix by `90°` clockwise in-place.
- **Pattern:** `Matrix Transformation`
- **Recognition:**
  - In-place matrix rotation
  - Square matrix property is important
  - Rotation can be decomposed into simpler transformations
- **Key Insight:**
  - A `90°` clockwise rotation can be achieved in two steps:
    rotate 90° clockwise = transpose + reverse rows
  1. Transpose matrix across main diagonal
  2. Reverse each row horizontally
  - While transposing, swap `matrix[i][j]` with `matrix[j][i]` for `i < j` to avoid double swapping
  - While reverseing rows, swap `matrix[i][j]` with `matrix[i][n-1-j]` for `j < n/2`

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

After Transpose:
[
 [1,4,7],
 [2,5,8],
 [3,6,9]
]

After Row Reverse:
[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
```

## 0054 - Spiral Matrix

- **Problem:** Return all elements of a matrix in spiral order:
  - left → right
  - top → bottom
  - right → left
  - bottom → top
- **Pattern:** `Matrix Traversal` / `Boundary Simulation`
- **Recognition:**
  - Traversal changes direction cyclically
  - Matrix layers shrink after each traversal
  - Requires careful boundary management
- **Key Insight:**
  - Maintain four boundaries:

  top, bottom, left, right
  - Traverse in four directions:
    1. left → right
    2. top → bottom
    3. right → left
    4. bottom → top
  - After each traversal, shrink corresponding boundary

- **Time Complexity:** `O(mn)`
- **Space Complexity:** `O(1)`
  - excluding output array

### Example

```text
Input:
matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

Traversal:
1 2 3
6 9
8 7
4
5

Output:
[1,2,3,6,9,8,7,4,5]
```

## 0059 - Spiral Matrix II

- **Problem:** Generate an `n x n` matrix filled with numbers from `1` to `n²` in spiral order.
- **Pattern:** `Matrix Traversal` / `Boundary Simulation`
- **Recognition:**
  - Spiral movement across matrix layers
  - Direction changes cyclically
  - Need controlled boundary shrinking
- **Key Insight:**
  - Maintain four boundaries:
    - `top`
    - `bottom`
    - `left`
    - `right`
  - Fill matrix in four directions repeatedly:
    1. left → right
    2. top → bottom
    3. right → left
    4. bottom → top
  - Shrink boundaries after each traversal
- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n²)`

### Example

```text
Input:
n = 3

Fill Order:
1 → 2 → 3
8 → 9 → 4
7 → 6 → 5

Output:
[
 [1,2,3],
 [8,9,4],
 [7,6,5]
]
```

## 0287 - Find the Duplicate Number

- **Problem:** Given an array containing `n + 1` integers where each integer is in the range `[1, n]`, return the duplicate number.
- **Pattern:** `Hash Set`
- **Recognition:**
  - Need duplicate detection
  - Fast membership lookup required
  - Values constrained to a known range
- **Key Insight:**
  - Maintain a set of seen numbers
  - While traversing:
    - if number already exists in set → duplicate found
    - otherwise add to set
  - First repeated value is the answer
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
nums = [1,3,4,2,2]

Traversal:
1 → add
3 → add
4 → add
2 → add
2 → already exists

Output:
2
```
