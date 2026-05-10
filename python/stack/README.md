# Stack

## Table of Contents

- [0020 - Valid Parentheses](#0020---valid-parentheses)

## 0020 - Valid Parentheses

- **Problem:** Given a string `s` containing only `'(){}[]'`, determine if it is valid (properly closed and correctly nested).
- **Pattern:** `Stack`
- **Recognition:** Need to match each closing bracket with the most recent unmatched opening bracket (LIFO order).
- **Key Insight:**
  - Use a stack to store opening brackets.
  - When encountering a closing bracket:
    - Stack must not be empty
    - Top of stack must match the corresponding opening bracket
  - At the end, stack must be empty for the string to be valid
  - `not stack` and `len(stack) == 0` are equivalent checks for an empty stack.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

---

### Example

```text
Input:
s = "()[]{}"

Process:
( → push
) → match → pop
[ → push
] → match → pop
{ → push
} → match → pop

Stack ends empty → valid
Output: True
```

---

### Key Insight

- Stack ensures correct nesting order (Last-In-First-Out)
- Always validate:
  - empty stack before pop
  - final stack must be empty

---

### Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brace_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif i in [')','}',']']:
                if not stack or brace_map[i] != stack.pop():
                    return False

        return len(stack) == 0
```
