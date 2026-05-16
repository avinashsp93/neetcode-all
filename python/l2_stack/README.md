# Stack

## Table of Contents

- [0020 - Valid Parentheses](#0020---valid-parentheses)
- [0682 - Baseball Game](#0682---baseball-game)

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
## 0682 - Baseball Game

- **Problem:** Evaluate a list of baseball score operations and return the total score.
- **Pattern:** `Stack`
- **Recognition:** 
  - Need access to recent history
  - Operations modify/remove previous entries
  - "Last valid score" is a strong stack indicator
- **Key Insight:**
  - Maintain a stack of valid scores
  - Operations:
    - `"C"` → remove previous score
    - `"D"` → double previous score
    - `"+"` → sum last two scores
    - integer → push new score
  - Stack naturally supports recent-score operations in `O(1)`
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
operations = ["5","2","C","D","+"]

Stack Process:
5   → [5]
2   → [5,2]
C   → [5]
D   → [5,10]
+   → [5,10,15]

Total:
5 + 10 + 15 = 30
Output: 30
```

## 1598 - Crawler Log Folder

- **Problem:** Given folder navigation logs:
  - `"../"` → move to parent folder
  - `"./"` → stay in current folder
  - `"x/"` → move into child folder
  return the minimum operations needed to return to the main folder.
- **Pattern:** `Stack Simulation`
- **Recognition:** 
  - Directory traversal/history tracking
  - Operations resemble push/pop behavior
  - Parent navigation strongly hints at stack usage
- **Key Insight:**
  - Moving into a folder increases depth
  - `"../"` decreases depth if possible
  - `"./"` changes nothing
  - Final depth equals operations needed to return to root
- **Time Complexity:** `O(n)`
- **Space Complexity:**  
  - Counter approach: `O(1)`
  - Stack approach: `O(n)`

### Example

```text
Input:
logs = ["d1/","d2/","../","d21/","./"]

Traversal:
root → d1 → d2 → d1 → d21

Current depth:
2

Output:
2
```