# Two Pointers

## Table of Contents

- [0344 - Reverse String](#0344---reverse-string)

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
