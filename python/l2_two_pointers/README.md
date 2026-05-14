# Two Pointers

## Table of Contents

- [0125 - Valid Palindrome](#0125---valid-palindrome)
- [0344 - Reverse String](#0344---reverse-string)


## 0125 - Valid Palindrome

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

---

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

---

### Key Insight

- Each swap fixes two positions at once.
- Only need `n // 2` iterations.
- In-place swapping avoids extra memory usage.

---
