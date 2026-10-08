# Stack

### Easy

- [0020 - Valid Parentheses](#0020---valid-parentheses)
- [0682 - Baseball Game](#0682---baseball-game)
- [1544 - Make The String Great](#1544---make-the-string-great)
- [1598 - Crawler Log Folder](#1598---crawler-log-folder)
- [2696 - Minimum String Length After Removing Substrings](#2696---minimum-string-length-after-removing-substrings)
- [3174 - Clear Digits](#3174---clear-digits)

### Medium

- [2390 - Removing Stars From a String](#2390---removing-removing-stars-from-a-string)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

<br><br>

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

## 1544 - Make The String Great

- **Problem:** Given a string, repeatedly remove adjacent pairs of the same letter in different cases (e.g., `'a'` and `'A'`) until no such pairs remain.
- **Pattern:** `Stack`
- **Recognition:**
  - Adjacent cancellation problem
  - Pairwise interaction between characters
  - Order matters → requires LIFO structure
- **Key Insight:**
  - Use a stack to track valid characters
  - If current character and stack top are the same letter in opposite cases → remove both
  - Case difference rule:

  |ord(a) - ord(A)| = 32
  - Otherwise, push character onto stack

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
s = "leEeetcode"

Process:
l e E e e t c o d e
   ↕ cancel (eE)
Result:
leetcode

Output:
"leetcode"
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

## 2696 - Minimum String Length After Removing Substrings

- **Problem:** Repeatedly remove occurrences of `"AB"` and `"CD"` from a string and return the minimum possible length after all removals.
- **Pattern:** `Stack`
- **Recognition:**
  - Characters may form removable pairs with adjacent previous characters.
  - Removing one pair can create new removable pairs.
  - A stack efficiently tracks the current valid characters while processing the string.
- **Key Insight:**
  - Traverse the string character by character.
  - Use a stack to store characters that have not been removed.
  - When encountering:
    - `"B"` and the top of the stack is `"A"`, remove the pair.
    - `"D"` and the top of the stack is `"C"`, remove the pair.
  - Otherwise, push the current character onto the stack.
  - After processing all characters, the stack contains the remaining string, and its size is the answer.

- **Time Complexity:** `O(n)`
  - Each character is pushed and popped at most once.
- **Space Complexity:** `O(n)`
  - In the worst case, all characters remain in the stack.

### Example

```text
Input:
s = "ABFCACDB"

Process:
AB -> removed
FCACDB
CD -> removed
FCAB
AB -> removed
FC

Remaining string:
"FC"

Output:
2
```

## 3174 - Clear Digits

- **Problem:** Remove each digit and the closest non-digit character immediately to its left. Return the resulting string after all removals.
- **Pattern:** `Stack`
- **Recognition:**
  - A character must be removed based on a future character (a digit).
  - Removals affect the most recent valid character.
  - A stack naturally keeps track of the nearest character to the left.
- **Key Insight:**
  - Traverse the string from left to right.
  - Store characters in a stack.
  - When a digit is encountered:
    - Remove the most recent letter from the stack.
    - Do not add the digit to the stack.
  - Otherwise, push the character onto the stack.
  - After processing all characters, the stack contains the final string.

- **Time Complexity:** `O(n)`
  - Each character is pushed and popped at most once.
- **Space Complexity:** `O(n)`
  - In the worst case, all characters remain in the stack.

### Example

```text
Input:
s = "abc3d2"

Process:
a -> [a]
b -> [a, b]
c -> [a, b, c]
3 -> remove c
d -> [a, b, d]
2 -> remove d

Remaining:
ab

Output:
"ab"
```

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  MEDIUM PROBLEMS
</h2>

<br><br>

## 0946 - Validate Stack Sequences

- **Problem:** Given two sequences `pushed` and `popped`, determine whether `popped` could be a valid pop order for a stack where elements are pushed in the order given by `pushed`.
- **Pattern:** `Stack + Simulation`
- **Recognition:**
  - The elements must be pushed in a fixed order.
  - At any point, we can only pop the element currently at the top of the stack.
  - Need to simulate the push/pop operations and check whether the required `popped` sequence can be produced.
  - Whenever the stack top matches the next element in `popped`, we should immediately pop it.
- **Key Insight:**
  - Push each element from `pushed` onto the stack.
  - After every push, check whether the top of the stack matches `popped[i]`.
  - If it matches, pop it and move `i` to the next element in `popped`.
  - Keep popping while the stack top matches the next required value.
  - At the end, if the stack is empty, the sequence is valid.
- **Time Complexity:** `O(n)`
  - Every element is pushed once and popped at most once.
- **Space Complexity:** `O(n)`
  - The stack can contain up to `n` elements.

### Example

```text
Input:
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]

Process:

Push 1:
stack = [1]

Push 2:
stack = [1,2]

Push 3:
stack = [1,2,3]

Push 4:
stack = [1,2,3,4]
top = 4 → matches popped[0]
pop 4

stack = [1,2,3]

Push 5:
stack = [1,2,3,5]
top = 5 → matches popped[1]
pop 5

top = 3 → matches popped[2]
pop 3

top = 2 → matches popped[3]
pop 2

top = 1 → matches popped[4]
pop 1

stack = []

Output:
True
```

## 2390 - Removing Stars From a String

- **Problem:** Given a string containing lowercase letters and `*`, remove each `*` along with the closest non-`*` character to its left.
- **Pattern:** `Stack`
- **Recognition:**
  - Each `*` removes the most recently added character.
  - This is a **Last In, First Out (LIFO)** behavior.
  - A stack is ideal because the most recently added character is always at the top.
- **Key Insight:**
  - Traverse the string from left to right.
  - If the character is not `*`, add it to the stack.
  - If the character is `*`, remove the most recent character using `pop()`.
  - At the end, join the remaining characters in the stack to form the result.
- **Time Complexity:** `O(n)`
  - Each character is added to or removed from the stack at most once.
- **Space Complexity:** `O(n)`
  - In the worst case, all characters are stored in the stack.

### Example

```text
Input:
s = "leet**cod*e"

Process:

l → [l]
e → [l,e]
e → [l,e,e]
t → [l,e,e,t]

* → remove t
* → remove e

c → [l,e,c]
o → [l,e,c,o]
d → [l,e,c,o,d]

* → remove d

e → [l,e,c,o,e]

Output:
"lecoe"
```