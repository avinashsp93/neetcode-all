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
- [0231 - Power of Two](#0231---power-of-two)
- [0268 - Missing Number](#0268---missing-number)
- [0278 - First Bad Version](#0278---first-bad-version)
- [0342 - Power of Four](#0342--power-of-four)
- [0383 - Ransom Note](#0383---ransom-note)
- [0389 - Find the Difference](#0389---find-the-difference)
- [0412 - Fizz Buzz](#0412---fizz-buzz)
- [0482 - License Key Formatting](#0482---license-key-formatting)
- [0509 - Fibonacci Number](#0509---fibonacci-number)
- [1137 - N-th Tribonacci Number](#1137---n-th-tribonacci-number)
- [1160 - Find Words That Can Be Formed by Characters](#1160---find-words-that-can-be-formed-by-characters)
- [1572 - Matrix Diagonal Sum](#1572---matrix-diagonal-sum)
- [1588 - Sum of All Odd Length Subarrays](#1588---sum-of-all-odd-length-subarrays)
- [1886 - Determine Whether Matrix Can Be Obtained By Rotation](#1886---determine-whether-matrix-can-be-obtained-by-rotation)
- [2133 - Check if Every Row and Column Contains All Numbers](#2133---check-if-every-row-and-column-contains-all-numbers)
- [2287 - Rearrange Characters to Form Target String](#2287---rearrange-characters-to-form-target-string)
- [2319 - Check if Matrix is X-Matrix](#2319---check-if-matrix-is-x-matrix)
- [3158 - Find the XOR of Numbers Which Appear Twice](#3158---find-the-xor-of-numbers-which-appear-twice)
- [3783 - Mirror Distance of an Integer](#3783---mirror-distance-of-an-integer)
- [3866 - First Unique Even Element](#3866---first-unique-even-element)
- [3870 - Count Commas in Range](#3870---count-commas-in-range)
- [3884 - First Matching Character From Both Ends](#3884---first-matching-character-from-both-ends)
- [3894 - Traffic Signal Color](#3894---traffic-signal-color)
- [3898 - Find the Degree of Each Vertex](#3898---find-the-degree-of-each-vertex)
- [3903 - First Stable Index](#3903---first-stable-index)
- [3908 - Valid Digit Number](#3908---valid-digit-number)
- [3912 - Valid Elements in an Array](#3912---valid-elements-in-an-array)
- [3917 - Count Indices with Opposite Parity](#3917---count-indices-with-opposite-parity)
- [3921 - Score Validator](#3921---score-validator)
- [3925 - Concatenate Array with Reverse](#3925---concatenate-array-with-reverse)
- [3931 - Check Adjacent Digit Differences](#3931---check-adjacent-digit-differences)
- [3936 - Minimum Swaps to Move Zeros to End](#3936---minimum-swaps-to-move-zeros-to-end)
- [3945 - Digit Frequency Score](#3945---digit-frequency-score)
- [3950 - Exactly One Consecutive Set Bits Pair](#3950---exactly-one-consecutive-set-bits-pair)
- [3954 - Sum of Compatible Numbers in Range I](#3954---sum-of-compatible-numbers-in-range-i)

### Medium

- [0034 - Find First and Last Position of Element in Sorted Array](#0034---find-first-and-last-position-of-element-in-sorted-array)
- [0036 - Valid Sudoku](#0036---valid-sudoku)
- [0048 - Rotate Image](#0048---rotate-image)
- [0054 - Spiral Matrix I](#0054---spiral-matrix-i)
- [0059 - Spiral Matrix II](#0059---spiral-matrix-ii)
- [0074 - Search a 2D Matrix](#0074---search-a-2d-matrix)
- [0151 - Reverse Words in a String](#0151---reverse-words-in-a-string)
- [0165 - Compare Version Numbers](#0165---compare-version-numbers)
- [0287 - Find the Duplicate Number](#0287---find-the-duplicate-number)
- [3895 - Count Digit Appearances](#3895---count-digit-appearances)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

<br><br>

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

## 0231 - Power of Two

- **Problem:** Determine whether a given integer `n` is a power of two.
- **Pattern:** `Bit Manipulation`
- **Recognition:**
  - The problem asks whether a number can be represented as `2^k`.
  - Powers of two have a unique binary representation.
  - Bitwise operations provide a constant-time solution.
- **Key Insight:**
  - A power of two contains exactly one set bit (`1`) in its binary representation.
  - Subtracting `1` from a power of two flips that set bit and all bits to its right.
  - Therefore:

    ```text
    n & (n - 1) = 0
    ```

    only when `n` has exactly one set bit.

  - Since non-positive numbers are not powers of two, first check `n > 0`.

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
n = 16

Binary:
16 = 10000
15 = 01111

10000
&
01111
=
00000

Output:
True
```

### Example 2

```text
Input:
n = 18

Binary:
18 = 10010
17 = 10001

10010
&
10001
=
10000

Result is not zero

Output:
False
```

### Example 3

```text
Input:
n = 1

Binary:
1 = 1

1 & 0 = 0

Output:
True
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

## 0342 -Power of Four

- **Problem:** Determine whether an integer `n` is a power of `4`.
- **Pattern:** `Bit Manipulation`
- **Recognition:**
  - Power-of-k validation
  - Constraints favor bitwise operations over loops/division
  - Power of 4 is a special subset of powers of 2
- **Key Insight:**
  - A power of 4 must satisfy **both**:
    1. It is a power of 2 (exactly one bit set)
    2. That bit is in an even position

  First check (power of 2):

  :contentReference[oaicite:0]{index=0}

  Then ensure the set bit is in a valid power-of-4 position using:

  ```python
  0x55555555
  ```

  Binary pattern:

```
01010101010101010101010101010101
```

which has 1s only in even bit positions.

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
n = 16

Binary:
10000

Power of 2?
10000 & 01111 = 0 ✓

Valid power-of-4 position?
10000 & 010101... ≠ 0 ✓

Output:
True
```

Notes

- **Strong interview pattern:**
  - power-of-two checks using bit tricks
  - additional constraint on bit position
- **Why the mask works:**
  - 4^0 = 1 -> bit position 0
  - 4^1 = 4 -> bit position 2
  - 4^2 = 16 -> bit position 4
  - 4^3 = 64 -> bit position 6
  - Powers of 4 have their single set bit only in even-indexed positions.
- **Common progression:**
  - Power of Two → single set bit
  - Power of Three → math/division approach
  - Power of Four → power of two + position check

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

## 1160 - Find Words That Can Be Formed by Characters

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

## 2287 - Rearrange Characters to Form Target String

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

## 3783 - Mirror Distance of an Integer

- **Problem:** Find the absolute difference between an integer and its digit-reversed (mirror) form.
- **Pattern:** `Math` / `String Manipulation`
- **Recognition:**
  - Requires reversing the digits of a number.
  - The result is the distance between the original and reversed values.
- **Key Insight:**
  - Convert the number to a string.
  - Reverse it using slicing (`[::-1]`).
  - Convert back to an integer and compute the absolute difference.

- **Time Complexity:** `O(d)`
  - `d` = number of digits in `n`
- **Space Complexity:** `O(d)`

### Example

```text
Input:
n = 123

Mirror:
321

Distance:
|321 - 123| = 198

Output:
198
```

## 3866 - First Unique Even Element

- **Problem:** Find the first even number that appears exactly once in the array. Return `-1` if no such element exists.
- **Pattern:** `Hash Map Counting`
- **Recognition:**
  - Need to identify unique elements.
  - Order of appearance matters.
  - Frequency counting followed by a second pass is a common approach.
- **Key Insight:**
  - Count the frequency of all even numbers using a hash map.
  - Traverse the array again in its original order.
  - Return the first even number whose frequency is `1`.
  - If no unique even number exists, return `-1`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(k)`
  - `k` = number of distinct even values

### Example

```text
Input:
nums = [4, 2, 4, 6, 2, 8]

Even Frequencies:
4 -> 2
2 -> 2
6 -> 1
8 -> 1

First unique even:
6

Output:
6
```

## 3870 - Count Commas in Range

- **Problem:** Count how many commas appear when writing all integers from `1` to `n` using standard comma-separated formatting.
- **Pattern:** `Math`
- **Key Insight:**
  - Numbers from `1` to `999` contain no commas.
  - Every number from `1000` to `n` contains exactly one comma.
  - Therefore, the count is:
    ```text
    max(0, n - 999)
    ```

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
n = 1005

Numbers with commas:
1000, 1001, 1002, 1003, 1004, 1005

Output:
6
```

## 3884 - First Matching Character from Both Ends

- **Problem:** Find the first index `i` such that the character at position `i` matches the character at its mirrored position from the end of the string.
- **Pattern:** `Two Pointers` / `Symmetric Comparison`
- **Recognition:**
  - Characters need to be compared with their mirrored counterparts.
  - The first valid index should be returned immediately.
  - Only one pass through the string is required.
- **Key Insight:**
  - For each index `i`, compare:
    ```text
    s[i] and s[n - i - 1]
    ```
  - If they match, return `i`.
  - If no matching mirrored pair exists, return `-1`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
s = "abca"

Comparisons:
s[0] = 'a', s[3] = 'a' ✓

First matching index:
0

Output:
0
```

## 3894 - Traffic Signal Color

- **Problem:** Determine the traffic signal color based on the value of `timer`.
- **Pattern:** `Conditional Logic`
- **Recognition:**
  - Output depends on a fixed set of conditions.
  - No iteration or complex data structures are required.
  - Each timer value range maps directly to a specific signal color.
- **Key Insight:**
  - Check the timer value against the defined rules:
    - `30 < timer <= 90` → `"Red"`
    - `timer == 30` → `"Orange"`
    - `timer == 0` → `"Green"`
    - Otherwise → `"Invalid"`
  - Return the corresponding signal color as soon as a condition is met.

- **Time Complexity:** `O(1)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
timer = 30

Check:
timer == 30

Output:
"Orange"
```

## 3898 - Find the Degree of Each Vertex

- **Problem:** Given an adjacency matrix of a graph, return the degree of each vertex.
- **Pattern:** `Matrix Traversal`
- **Key Insight:**
  - In an adjacency matrix, each row represents a vertex.
  - The degree of a vertex is the sum of the values in its row.
  - Compute the sum for each row and store it in the result.

- **Time Complexity:** `O(V²)`
- **Space Complexity:** `O(V)`
  - for the output array

### Example

```text
Input:
[
 [0, 1, 1],
 [1, 0, 0],
 [1, 0, 0]
]

Row sums:
[2, 1, 1]

Output:
[2, 1, 1]
```

## 3903 - First Stable Index

- **Problem:** Find the smallest index `i` such that the difference between the maximum value seen up to `i` and the minimum value seen from `i` to the end is at most `k`.
- **Pattern:** `Prefix Maximum` / `Suffix Minimum`
- **Recognition:**
  - Need information from both the left and right side of every index.
  - Recomputing maximums and minimums for each index would be inefficient.
  - Prefix and suffix arrays allow constant-time validation per index.
- **Key Insight:**
  - Build a `maxScores` array where:

    `maxScores[i] = max(nums[0...i])`

  - Build a `minScores` array where:

    `minScores[i] = min(nums[i...n-1])`

  - For each index `i`, check whether:

    ```text
    maxScores[i] - minScores[i] <= k
    ```

  - Return the first index that satisfies the condition.
  - If no valid index exists, return `-1`.

- **Time Complexity:** `O(n)`
  - One pass for prefix maximums, one pass for suffix minimums, and one validation pass.
- **Space Complexity:** `O(n)`
  - For the prefix and suffix arrays.

### Example

```text
Input:
nums = [3, 1, 4, 2]
k = 2

Prefix maximums:
[3, 3, 4, 4]

Suffix minimums:
[1, 1, 2, 2]

Differences:
3 - 1 = 2 ✓
3 - 1 = 2 ✓
4 - 2 = 2 ✓
4 - 2 = 2 ✓

First valid index:
0

Output:
0
```

## 3908 - Valid Digit Number

- **Problem:** Determine whether digit `x` appears in the decimal representation of `n`, but **not as the first digit**.
- **Pattern:** `String Conversion` / `Digit Inspection`
- **Recognition:**
  - Need to inspect individual digits of a number.
  - Position of a digit matters.
  - String conversion provides simple digit access.
- **Key Insight:**
  - Convert `n` to a string.
  - The first digit must not be `x`.
  - The digit `x` must appear somewhere after the first position.
  - Check both conditions directly:
    ```python
    str(x) != str(n)[0] and str(x) in str(n)[1:]
    ```

- **Time Complexity:** `O(d)`
  - `d` = number of digits in `n`
- **Space Complexity:** `O(d)`
  - due to string conversion

### Example

```text
Input:
n = 3123
x = 2

Check:
First digit = '3'
Remaining digits = '123'

'2' != '3'  -> True
'2' in '123' -> True

Output:
True
```

## 3912 - Valid Elements in an Array

- **Problem:** Find all elements that are greater than every element to their left and greater than every element to their right.
- **Pattern:** `Prefix Maximum` / `Suffix Maximum`
- **Recognition:**
  - Need to compare each element against all elements on both sides.
  - Direct comparison with every other element would be inefficient.
  - Prefix and suffix information can be precomputed to make validation efficient.
- **Key Insight:**
  - Traverse from left to right and mark elements that are greater than all previous elements.
  - Traverse from right to left and mark elements that are greater than all elements to their right.
  - An element is valid only if it satisfies both conditions.
  - Collect all elements that are marked valid from both directions.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
  - for the prefix and suffix marker arrays

### Example

```text
Input:
nums = [1, 3, 2, 5, 4]

Greater than all elements to the left:
[True, True, False, True, False]

Greater than all elements to the right:
[False, True, False, True, True]

Valid elements:
3, 5

Output:
[3, 5]
```

## 3917 - Count Indices with Opposite Parity

- **Problem:** For each index `i`, count how many elements to its right have the opposite parity (even vs. odd) and return the resulting array.
- **Pattern:** `Reverse Traversal` / `Counting`
- **Recognition:**
  - Need information about elements that appear to the right of the current index.
  - Counting is based on a simple property (parity).
  - A reverse traversal allows maintaining running counts efficiently.
- **Key Insight:**
  - Traverse the array from right to left.
  - Maintain:
    - `evenC` = number of even elements seen so far
    - `oddC` = number of odd elements seen so far
  - For each element:
    - If it is even, all previously seen odd numbers contribute to its answer.
    - If it is odd, all previously seen even numbers contribute to its answer.
  - Store the counts while traversing backwards, then reverse the result to restore the original order.

- **Time Complexity:** `O(n)`
  - Single pass through the array plus one reversal.
- **Space Complexity:** `O(n)`
  - For the output array.

### Example

```text
Input:
nums = [2, 1, 4, 3]

Traverse from right to left:

3 (odd):
evenC = 0
answer = 0

4 (even):
oddC = 1
answer = 1

1 (odd):
evenC = 1
answer = 1

2 (even):
oddC = 2
answer = 2

Collected (reverse order):
[0, 1, 1, 2]

Reverse:
[2, 1, 1, 0]

Output:
[2, 1, 1, 0]
```

## 3921 - Score Validator

- **Problem:** Process a sequence of cricket scoring events and return the final score and number of wickets lost.
- **Pattern:** `Simulation` / `Event Processing`
- **Recognition:**
  - Input consists of sequential events that modify a running state.
  - Multiple event types have different effects on score and wickets.
  - Requires maintaining cumulative values while iterating once through the input.
- **Key Insight:**
  - Track two variables:
    - `score` → total runs scored
    - `wickets` → total wickets lost
  - Process each event:
    - `"W"` → increment wickets
    - `"WD"` or `"NB"` → add 1 run
    - Numeric string (`"0"`–`"6"`) → add corresponding runs
  - Cricket innings end after 10 wickets, so return immediately when the 10th wicket falls.

- **Time Complexity:** `O(n)`
  - `n` = number of events
- **Space Complexity:** `O(1)`
  - only a few variables are used

### Example

```text
Input:
events = ["1", "4", "WD", "W", "6", "NB"]

Processing:
score = 0, wickets = 0

"1"  -> score = 1
"4"  -> score = 5
"WD" -> score = 6
"W"  -> wickets = 1
"6"  -> score = 12
"NB" -> score = 13

Output:
[13, 1]
```

### Early Termination Example

```text
Input:
events = ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "6"]

Processing:
10th wicket falls

Innings ends immediately.

Output:
[0, 10]
```

## 3925 - Concatenate Array with Reverse

- **Problem:** Return a new array formed by concatenating `nums` with its reversed version.
- **Pattern:** `Array Manipulation`
- **Recognition:**
  - Need to create a transformed copy of the input array.
  - Reverse order of elements is required.
  - Result is a combination of the original array and its reverse.
- **Key Insight:**
  - Use Python slicing `nums[::-1]` to create a reversed copy of the array.
  - Concatenate the original array with the reversed array using `+`.
  - This produces a new array containing all elements followed by the same elements in reverse order.

- **Time Complexity:** `O(n)`
  - Creating the reversed copy takes `O(n)`.
  - Concatenation also takes `O(n)`.
- **Space Complexity:** `O(n)`
  - A new array of size `2n` is created.

### Example

```text
Input:
nums = [1, 2, 3]

Reverse:
[3, 2, 1]

Concatenation:
[1, 2, 3] + [3, 2, 1]

Output:
[1, 2, 3, 3, 2, 1]
```

### Example 2

```text
Input:
nums = [5, 10]

Reverse:
[10, 5]

Concatenation:
[5, 10] + [10, 5]

Output:
[5, 10, 10, 5]
```

## 3931 - Check Adjacent Digit Differences

- **Problem:** Determine whether the absolute difference between every pair of adjacent digits in a string is at most `2`.
- **Pattern:** `Sequential Traversal` / `Adjacent Comparison`
- **Recognition:**
  - Need to compare neighboring elements in a sequence.
  - Validation depends on a condition holding for every adjacent pair.
  - Can stop early as soon as an invalid pair is found.
- **Key Insight:**
  - Iterate through the string from left to right.
  - For each index `i`, compare digit `s[i]` with `s[i + 1]`.
  - If their absolute difference exceeds `2`, return `False`.
  - If all adjacent pairs satisfy the condition, return `True`.

- **Time Complexity:** `O(n)`
  - `n` = length of the string
- **Space Complexity:** `O(1)`
  - only a few variables are used

### Example

```text
Input:
s = "12345"

Comparisons:
|1 - 2| = 1
|2 - 3| = 1
|3 - 4| = 1
|4 - 5| = 1

All differences are ≤ 2

Output:
True
```

### Example 2

```text
Input:
s = "1358"

Comparisons:
|1 - 3| = 2
|3 - 5| = 2
|5 - 8| = 3

Difference exceeds 2

Output:
False
```

## 3936 - Minimum Swaps to Move Zeros to End

- **Problem:** Given a binary array containing `0`s and `1`s, determine the minimum number of swaps required to move all `0`s to the end of the array.
- **Pattern:** `Counting` / `Greedy Observation`
- **Recognition:**
  - The final positions of all `0`s are known: they must occupy the last `k` positions, where `k` is the number of zeroes.
  - Swapping can place a misplaced `1` in the correct position with a `0` from elsewhere.
  - Only the elements in the target suffix need to be inspected.
- **Key Insight:**
  - Count the total number of zeroes, `k`.
  - In the desired arrangement, the last `k` positions should all contain `0`.
  - Examine those last `k` positions:
    - Every `1` found there is misplaced.
    - Each misplaced `1` requires exactly one swap with a `0` outside the suffix.
  - Therefore, the answer is simply the number of non-zero elements in the last `k` positions.

- **Time Complexity:** `O(n)`
  - Counting zeroes and scanning the target suffix each take linear time.
- **Space Complexity:** `O(1)`
  - excluding the temporary slice created by Python

### Example

```text
Input:
nums = [0, 1, 0, 1, 1]

Number of zeroes:
k = 2

Target suffix (last 2 positions):
[1, 1]

Misplaced elements:
2 ones

Minimum swaps:
2

Output:
2
```

### Example 2

```text
Input:
nums = [1, 1, 1, 0, 0]

Number of zeroes:
k = 2

Target suffix (last 2 positions):
[0, 0]

Misplaced elements:
0

Minimum swaps:
0

Output:
0
```

## 3945 - Digit Frequency Score

- **Problem:** Calculate the digit frequency score of an integer `n`, where each digit contributes:

  `digit × frequency of that digit`

- **Pattern:** `Hash Map Counting`
- **Recognition:**
  - Need to count occurrences of elements.
  - Each unique digit contributes based on its frequency.
  - A hash map (dictionary) is a natural way to store counts.
- **Key Insight:**
  - Convert the number to a string and count the frequency of each digit using a dictionary.
  - For every digit-frequency pair:

    `contribution = digit × frequency`

  - Sum all contributions to obtain the final score.

- **Time Complexity:** `O(d)`
  - `d` = number of digits in `n`
- **Space Complexity:** `O(k)`
  - `k` = number of distinct digits (`≤ 10`)

### Example

```text
Input:
n = 122333

Digit Frequencies:
1 -> 1
2 -> 2
3 -> 3

Score:
(1 × 1) + (2 × 2) + (3 × 3)
= 1 + 4 + 9
= 14

Output:
14
```

### Example 2

```text
Input:
n = 5555

Digit Frequencies:
5 -> 4

Score:
5 × 4
= 20

Output:
20
```

## 3950 - Exactly One Consecutive Set Bits Pair

- **Problem:** Determine whether the binary representation of `n` contains exactly one occurrence of two consecutive set bits (`11`).
- **Pattern:** `Bit Manipulation`
- **Recognition:**
  - Requires analyzing the binary representation of a number.
  - Looking for a specific bit pattern (`11`).
  - Bitwise operations can inspect adjacent bits efficiently.
- **Key Insight:**
  - Examine the last two bits using:
    ```text
    n & 3
    ```
    where `3` is `11` in binary.
  - If the result is `3`, the current two-bit window is `11`.
  - Right shift the number one bit at a time and count how many times `11` appears.
  - Return `True` only if exactly one such pair exists.

- **Time Complexity:** `O(log n)`
  - One iteration per bit.
- **Space Complexity:** `O(1)`

### Example

```text
Input:
n = 13

Binary:
1101

Windows:
01 -> not a pair
10 -> not a pair
11 -> one pair

Count = 1

Output:
True
```

## 3954 - Sum of Compatible Numbers in Range I

- **Problem:** Find the sum of all integers `x` in the range `[n-k, n+k]` such that `n` and `x` have no common set bits.
- **Pattern:** `Bit Manipulation` / `Simulation`
- **Recognition:**
  - Need to evaluate every number in a given range.
  - Compatibility is determined using a bitwise condition.
  - The condition `n & x == 0` indicates no overlapping set bits.
- **Key Insight:**
  - Iterate through all numbers in the range:
    ```text
    [max(0, n-k), n+k]
    ```
  - For each number `x`, check:
    ```text
    n & x == 0
    ```
  - If true, add `x` to the running sum.
  - Return the final accumulated sum.

- **Time Complexity:** `O(k)`
  - The range contains at most `2k + 1` numbers.
- **Space Complexity:** `O(1)`

### Example

```text
Input:
n = 5
k = 2

Range:
[3, 4, 5, 6, 7]

Binary:
5 = 101

3 = 011 -> 101 & 011 ≠ 0
4 = 100 -> 101 & 100 ≠ 0
5 = 101 -> 101 & 101 ≠ 0
6 = 110 -> 101 & 110 ≠ 0
7 = 111 -> 101 & 111 ≠ 0

No compatible numbers.

Output:
0
```

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  MEDIUM PROBLEMS
</h2>

<br><br>

## 0034 - Find First and Last Position of Element in Sorted Array

- **Problem:** Given a sorted array `nums` and a target value, return the starting and ending position of the target in the array. If the target is not found, return `[-1, -1]`.
- **Pattern:** `Binary Search`
- **Recognition:**
  - Sorted array allows for binary search
  - Need to find both first and last occurrence
  - Two-pass binary search approach is common
- **Key Insight:**
  - Perform binary search to find the leftmost index of the target
  - Perform binary search to find the rightmost index of the target
  - If either search fails, return `[-1, -1]`
- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [5,7,7,8,8,10]
target = 8
Leftmost index of 8 is 3
Rightmost index of 8 is 4
Output:
[3,4]
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

## 0048 - Rotate Image

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

## 0054 - Spiral Matrix I

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

## 0074 - Search a 2D Matrix

- **Problem:** Determine whether a target value exists in a matrix where:
  - Each row is sorted in ascending order.
  - The first element of each row is greater than the last element of the previous row.
- **Pattern:** `Binary Search` / `Floor Binary Search`
- **Recognition:**
  - Rows are ordered relative to each other.
  - Each row is individually sorted.
  - The matrix can be searched by first locating the candidate row, then searching within that row.
- **Key Insight:**
  - Perform a binary search on the first column to find the **floor row**:
    - The last row whose first element is less than or equal to the target.
    - Refer to the `searchBinary` code for implementation details.
  - If the target equals the first element of a row, return `True`.
  - Once the candidate row is found, perform a second binary search within that row.
  - If the target is found, return `True`; otherwise return `False`.

- **Time Complexity:** `O(log m + log n)`
  - `m` = number of rows
  - `n` = number of columns
- **Space Complexity:** `O(1)`

### Example

```text
Input:
matrix =
[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]

target = 16

Step 1:
Binary search rows using first column.
Candidate row = [10, 11, 16, 20]

Step 2:
Binary search within the row.

16 found.

Output:
True
```

## 0151 - Reverse Words in a String

- **Problem:** Reverse the order of words in a string while removing leading, trailing, and extra spaces between words.
- **Pattern:** `String Manipulation`
- **Recognition:**
  - Word-level reversal (not character reversal)
  - Input may contain irregular spacing
  - Need normalized output formatting
- **Key Insight:**
  - `split()` automatically:
    - removes leading/trailing spaces
    - collapses multiple spaces
    - extracts words
  - Reverse the list of words
  - Join them back with a single space
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
"  hello   world  "

split():
["hello", "world"]

reverse:
["world", "hello"]

Output:
"world hello"
```

## 0165 - Compare Version Numbers

- **Problem:** Compare two version strings and return:
  - `1` if `version1 > version2`
  - `-1` if `version1 < version2`
  - `0` if they are equal
- **Pattern:** `Two Pointers` / `String Parsing`
- **Recognition:**
  - Structured string comparison
  - Components separated by delimiters (`.`)
  - Leading zeros should be ignored
- **Key Insight:**
  - Split both versions into revision numbers
  - Compare corresponding revisions from left to right
  - Convert each revision to an integer:
    - `"001"` and `"1"` become equal
  - If one version has remaining revisions, they only matter if any are non-zero
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(n + m)`
  - due to storing split components

### Example

```text
Input:
version1 = "1.01"
version2 = "1.001"

Compare:
1 == 1
1 == 1

Output:
0


Input:
version1 = "1.0"
version2 = "1.0.1"

Compare:
1 == 1
0 == 0

Remaining:
1 > 0

Output:
-1
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

## 3895 - Count Digit Appearances

- **Problem:** Count how many times a given digit appears across all numbers in an array.
- **Pattern:** `Math` / `Digit Extraction`
- **Recognition:**
  - Need to inspect every digit of every number.
  - Converting to strings is possible, but arithmetic operations provide a direct solution.
  - Digits can be extracted using modulo and integer division.
- **Key Insight:**
  - For each number:
    - Handle the special case `0` when the target digit is also `0`.
    - Repeatedly extract the last digit using `% 10`.
    - If it matches the target digit, increment the count.
    - Remove the last digit using `// 10`.
  - Continue until all digits have been processed.

- **Time Complexity:** `O(total_digits)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [12, 23, 202]
digit = 2

Occurrences:
12  -> 1
23  -> 1
202 -> 2

Output:
4
```
