# Two Pointers

## Table of Contents

### Easy

- [Table of Contents](#table-of-contents)
- [0125 - Valid Palindrome I](#0125---valid-palindrome-i)
- [0344 - Reverse String](#0344---reverse-string)
- [0680 - Valid Palindrome II](#0680---valid-palindrome-ii)

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
