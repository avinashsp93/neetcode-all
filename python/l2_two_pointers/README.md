# Two Pointers

### Easy
- [0026 - Remove Duplicates from Sorted Array](#0026---remove-duplicates-from-sorted-array)
- [0088 - Merge Sorted Array](#0088---merge-sorted-array)
- [0125 - Valid Palindrome I](#0125---valid-palindrome-i)
- [0283 - Move Zeroes](#0283---move-zeroes)
- [0344 - Reverse String](#0344---reverse-string)
- [0680 - Valid Palindrome II](#0680---valid-palindrome-ii)
- [1768 - Merge Strings Alternately](#1768---merge-strings-alternately)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

<br><br>

## 0026 - Remove Duplicates from Sorted Array

- **Problem:** Remove duplicates from a sorted array in-place and return the number of unique elements.
- **Pattern:** `Two Pointers` / `Fast & Slow Pointers`
- **Recognition:**
  - The array is already sorted.
  - Duplicate values appear consecutively.
  - The array must be modified in-place with `O(1)` extra space.
- **Key Insight:**
  - Use two pointers:
    - `slow` tracks the position of the last unique element.
    - `fast` scans the array for new unique values.
  - Whenever `nums[fast]` differs from `nums[slow]`:
    - Advance `slow`.
    - Copy `nums[fast]` to `nums[slow]`.
  - After one pass, the first `slow + 1` elements contain all unique values in sorted order.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [1, 1, 2, 2, 3]

Traversal:
slow = 0
fast scans the array

Unique values copied:
[1, 2, 3, _, _]

Output:
3
```

## 0088 - Merge Sorted Array

- **Problem:** Merge two sorted arrays `nums1` and `nums2` into a single sorted array stored inside `nums1`.
- **Pattern:** `Two Pointers` / `Reverse Traversal`
- **Recognition:**
  - Two sorted arrays need to be merged.
  - `nums1` already has enough extra space to hold all elements.
  - Writing from the front would overwrite unprocessed values.
- **Key Insight:**
  - Use three pointers:
    - `p1` → last valid element in `nums1`
    - `p2` → last element in `nums2`
    - `p` → last position in `nums1`
  - Compare elements from the end of both arrays.
  - Place the larger element at position `p`.
  - Move the corresponding pointer and continue.
  - If elements remain in `nums2`, copy them into `nums1`.
  - No need to copy remaining elements from `nums1` since they are already in the correct position.

- **Time Complexity:** `O(m + n)`
  - Each element is processed at most once.
- **Space Complexity:** `O(1)`
  - Merging is performed in-place.

### Example

```text
Input:
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

Pointers:
p1 = 2 (3)
p2 = 2 (6)
p  = 5

Step 1:
6 > 3
nums1[5] = 6

[1,2,3,0,0,6]

Step 2:
5 > 3
nums1[4] = 5

[1,2,3,0,5,6]

Step 3:
3 > 2
nums1[3] = 3

[1,2,3,3,5,6]

Step 4:
2 == 2
nums1[2] = 2

[1,2,2,3,5,6]

Remaining:
Copy 2 from nums2

Output:
[1,2,2,3,5,6]
```

### Why Reverse Traversal?

```text
nums1 = [1,2,3,0,0,0]

If we merge from the front,
values in nums1 may be overwritten before being compared.

By filling from the end,
all unprocessed elements remain intact.
```

## 0125 - Valid Palindrome I

- **Problem:** Determine whether a string is a palindrome after:
  - removing non-alphanumeric characters
  - ignoring letter casing
- **Pattern:** `Two Pointers`
- **Recognition:**
  - Need comparison from both ends toward center
  - Characters may need to be skipped conditionally
  - In-place traversal preferred over rebuilding strings
- **Key Insight:**
  - Use two pointers:
    - left pointer moves forward
    - right pointer moves backward
  - Skip non-alphanumeric characters
  - Compare lowercase versions of valid characters
  - If mismatch occurs → not a palindrome
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
s = "A man, a plan, a canal: Panama"

Filtered comparison:
amanaplanacanalpanama

Output:
True
```

## 0283 - Move Zeroes

- **Problem:** Move all `0`s to the end of the array while maintaining the relative order of non-zero elements. Modify the array in-place.
- **Pattern:** `Two Pointers`
- **Recognition:**
  - Need stable rearrangement of elements
  - Move a specific value (`0`) while preserving order of others
  - In-place modification required
- **Key Insight:**
  - Use two pointers:
    - `r` scans every element
    - `l` tracks the next position for a non-zero value
  - Whenever a non-zero is found:
    - swap it into position `l`
    - advance `l`
  - l is a slow pointer and r is a fast pointer
  - All positions before `l` contain non-zero values in correct order
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
[0,1,0,3,12]

l=0, r=1 → swap 1 with 0
[1,0,0,3,12]

l=1, r=3 → swap 3 with 0
[1,3,0,0,12]

l=2, r=4 → swap 12 with 0
[1,3,12,0,0]

Output:
[1,3,12,0,0]
```

## 0344 - Reverse String

- **Problem:** Reverse a list of characters in-place.
- **Pattern:** `Two Pointers / In-place Swapping`
- **Recognition:** Need to swap elements symmetrically from both ends of the array.
- **Key Insight:**
  - Use two pointers: one starting from the beginning and one from the end.
  - Swap elements until pointers meet in the middle.
  - Only iterate through half the array.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
s = ["h","e","l","l","o"]

Swaps:
h ↔ o
e ↔ l

Result:
["o","l","l","e","h"]
```

## 0680 - Valid Palindrome II

- **Problem:** Given a string, determine if it can become a palindrome after deleting at most one character.
- **Pattern:** `Two Pointers` / `Greedy + Subproblem Check`
- **Recognition:**
  - Standard palindrome check with a twist
  - First mismatch triggers a “one deletion allowed” decision
  - Must validate two possible skip cases
- **Key Insight:**
  - Use two pointers from both ends:
    - if characters match → continue, and move inward (subproblem reduces)
    - if mismatch → try skipping either left or right character
  - Only one deletion is allowed, so we check two possibilities:
    1. skip left character
    2. skip right character
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (ignoring slicing overhead)

### Example

```text
Input:
s = "abca"

Check:
a == a → ok
b != c → mismatch

Try:
remove 'b' → "aca" (valid palindrome)

Output:
True
```

## 0977 - Squares of a Sorted Array

- **Problem:** Return an array of the squares of each number, sorted in non-decreasing order.
- **Pattern:** `Two Pointers`
- **Recognition:**
  - Squaring negative numbers can make them larger than positive numbers.
  - The largest square must come from one of the two ends of the sorted array.
  - Two pointers can build the sorted result in a single pass.
- **Key Insight:**
  - Initialize two pointers:
    - `left` at the beginning.
    - `right` at the end.
  - Compare the absolute values at both ends.
  - Append the larger square to the result.
  - Move the corresponding pointer inward.
  - Since the largest squares are added first, reverse the result at the end.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
nums = [-4, -1, 0, 3, 10]

Compare:
|-4| vs |10| -> 100
|-4| vs |3|  -> 16
|-1| vs |3|  -> 9
...

Reversed result:
[0, 1, 9, 16, 100]

Output:
[0, 1, 9, 16, 100]
```

## 1768 - Merge Strings Alternately

- **Problem:** Merge two strings by alternating characters from each string, starting with the first string. If one string is longer, append its remaining characters at the end.
- **Pattern:** `Two Pointers`
- **Recognition:**
  - Need to traverse two sequences simultaneously.
  - Characters are consumed in order from both strings.
  - Remaining characters from the longer string must be handled after the main traversal.
- **Key Insight:**
  - Use two pointers:
    - `p1` for `word1`
    - `p2` for `word2`
  - While both pointers are within bounds:
    - Append one character from `word1`
    - Append one character from `word2`
    - Advance both pointers
  - After the loop:
    - If `word1` is exhausted, append the remaining part of `word2`
    - If `word2` is exhausted, append the remaining part of `word1`

- **Time Complexity:** `O(n + m)`
  - `n` = length of `word1`
  - `m` = length of `word2`
- **Space Complexity:** `O(n + m)`
  - for the output string

### Example

```text
Input:
word1 = "abc"
word2 = "pqr"

Merge:
a + p
b + q
c + r

Output:
"apbqcr"
```

### Example 2

```text
Input:
word1 = "ab"
word2 = "pqrs"

Merge:
a + p
b + q

Remaining:
rs

Output:
"apbqrs"
```

### Example 3

```text
Input:
word1 = "abcd"
word2 = "pq"

Merge:
a + p
b + q

Remaining:
cd

Output:
"apbqcd"
```
