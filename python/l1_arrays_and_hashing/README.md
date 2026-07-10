# Arrays & Hashing

### Easy

- [0001 - Two Sum](#0001---two-sum)
- [0014 - Longest Common Prefix](#0014---longest-common-prefix)
- [0027 - Remove Element](#0027---remove-element)
- [0058 - Length of Last Word](#0058---length-of-last-word)
- [0118 - Pascal's Triangle](#0118---pascals-triangle)
- [0169 - Majority Element](#0169---majority-element)
- [0205 - Isomorphic Strings](#0205---isomorphic-strings)
- [0217 - Contains Duplicate](#0217---contains-duplicate)
- [0242 - Valid Anagram](#0242---valid-anagram)
- [0290 - Word Pattern](#0290---word-pattern)
- [0383 - Ransom Note](#0383---ransom-note)
- [0392 - Is Subsequence](#0392---is-subsequence)
- [0448 - Find All Numbers Disappeared in an Array](#0448---find-all-numbers-disappeared-in-an-array)
- [0485 - Max Consecutive Ones](#0485---max-consecutive-ones)
- [0496 - Next Greater Element I](#0496---next-greater-element-i)
- [0605 - Can Place Flowers](#0605---can-place-flowers)
- [0724 - Find Pivot Index](#0724---find-pivot-index)
- [0896 - Monotonic Array](#0896---monotonic-array)
- [0929 - Unique Email Addresses](#0929---unique-email-addresses)
- [1002 - Find Common Characters](#1002---find-common-characters)
- [1189 - Maximum Number of Balloons](#1189---maximum-number-of-balloons)
- [1299 - Replace Elements with Greatest Element on Right Side](#1299---replace-elements-with-greatest-element-on-right-side)
- [1394 - Find Lucky Integer in an Array](#1394---find-lucky-integer-in-an-array)
- [1408 - String Matching in an Array](#1408---string-matching-in-an-array)
- [1752 - Check if Array Is Sorted and Rotated](#1752---check-if-array-is-sorted-and-rotated)
- [1800 - Maximum Ascending Subarray Sum](#1800---maximum-ascending-subarray-sum)
- [2053 - Kth Distinct String in an Array](#2053---kth-distinct-string-in-an-array)
- [2206 - Divide Array Into Equal Pairs](#2206---divide-array-into-equal-pairs)
- [2678 - Number of Senior Citizens](#2678---number-of-senior-citizens)
- [2965 - Find Missing and Repeated Values](#2965---find-missing-and-repeated-values)
- [3105 - Longest Strictly Increasing or Strictly Decreasing Subarray](#3105---longest-strictly-increasing-or-strictly-decreasing-subarray)
- [3110 - Score of a String](#3110---score-of-a-string)
- [3151 - Special Array I](#3151---special-array-i)
- [3442 - Maximum Difference Between Even and Odd Frequency](#3442---maximum-difference-between-even-and-odd-frequency)

<br><br>

<h2 style="text-align: center;text-transform: uppercase;">
  EASY PROBLEMS
</h2>

<br><br>

## 0001 - Two Sum

- **Problem**: Given an array of integers and a target sum, find the indices of the two numbers that add up to the target.
- **Pattern**: Hash Map
- **Key Insight**:
  - Use a hash map to store the number as key and its index as value.
  - Instead of checking every pair, store previously seen numbers and check whether the required complement already exists.
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Example**:

  ```Text
    Input: nums = [2, 7, 11, 15], target = 9

  Dictionary after processing:
  {
    2: 0,  # number: index
    7: 1,
    11: 2,
    15: 3
  }
  ```

## 0014 - Longest Common Prefix

- **Problem:** Find the longest common prefix string among an array of strings.
- **Pattern:** `Horizontal Scanning`
- **Recognition:** Need to compare characters position-by-position across multiple strings.
- **Key Insight:**
  - The common prefix can only be as long as the shortest string.
  - Compare characters at the same index across all strings.
  - Stop immediately when a mismatch is found.
- **Time Complexity:** `O(n * m)`
  - `n` = number of strings
  - `m` = length of shortest string
- **Space Complexity:** `O(1)` (excluding output string)

### Example

```text
Input:
["flower", "flow", "flight"]

Comparison:

Index 0 → all have 'f'
Index 1 → all have 'l'
Index 2 → mismatch ('o' vs 'i')

Output:
"fl"
```

## 0027 - Remove Element

- **Problem:** Remove all occurrences of a given value in-place and return the number of remaining elements.
- **Pattern:** `Two Pointers`
- **Recognition:** Need in-place modification while preserving remaining elements.
- **Key Insight:**
  - Use one pointer to traverse the array.
  - Use another pointer (`k`) to track the next valid insertion position.
  - Whenever a non-target value is found, place it at index `k` and increment `k`.
  - `k` will be the slow moving pointer and i will be the fast moving pointer. Both be moving forward, but `k` only moves when we find a non-target value.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [3, 2, 2, 3]
val = 3

Traversal:

3 → skip
2 → place at nums[0]
2 → place at nums[1]
3 → skip

Modified array:
[2, 2, _, _]

Output:
k = 2
```

## 0058 - Length of Last Word

- **Problem:** Given a string `s`, return the length of the last word in the string.
- **Pattern:** `Backward Traversal / Two Pointers`
- **Recognition:** Need to ignore trailing spaces and then count characters until the first space.
- **Key Insight:**
  - Start from the end of the string.
  - Skip all trailing spaces first.
  - Then count characters until a space or beginning of string is reached.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
s = "Hello World   "

Traversal from end:

Skip spaces → reach 'd'
Count until space:
"World" → length = 5

Output:
5
```

## 0118 - Pascal's Triangle

- **Problem:** Generate the first `numRows` of Pascal’s Triangle.
- **Pattern:** `Simulation` / `Dynamic Programming`
- **Recognition:**
  - Need to build rows based on previous row values
  - Current state depends directly on previous computed state
  - Triangle growth pattern where edge values are always `1`
- **Key Insight:**
  - Each row can be generated by summing adjacent pairs from the previous row
  - Padding the previous row with zeros (`[0, ...row, 0]`) simplifies edge handling
  - Avoids boundary checks for first and last elements
- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n²)`

### Example

```text
Previous Row: [1, 3, 3, 1]

Padded:
[0, 1, 3, 3, 1, 0]

Adjacent sums:
1, 4, 6, 4, 1

Next Row:
[1, 4, 6, 4, 1]
```

## 0169 - Majority Element

- **Problem:** Given an array `nums`, return the element that appears more than `⌊n / 2⌋` times.
- **Pattern:** `Greedy` / `Boyer-Moore Voting Algorithm`
- **Recognition:**
  - Problem guarantees a majority element exists
  - Need better than hash map counting
  - Frequent hint toward `O(1)` space optimization
- **Key Insight:**
  - Majority element can "cancel out" all other elements combined
  - Maintain:
    - `candidate` → potential majority element
    - `count` → voting balance
  - When count becomes `0`, choose a new candidate
  - Matching element increases vote, different element decreases vote
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [2,2,1,1,1,2,2]

Voting Process:
2 → count = 1
2 → count = 2
1 → count = 1
1 → count = 0
1 → candidate = 1
2 → count = 0
2 → candidate = 2

Output:
2

To write the code for this algorithm:
life cycle of count and result with input:
input =    [2,2,1,1,1,2,2]
result = [0,2,2,2,2,1,1,2]
count =  [0,1,2,1,0,1,0,1]




```

## 0205 - Isomorphic Strings

- **Problem:** Given two strings `s` and `t`, determine if they are isomorphic (each character in `s` can map to a unique character in `t` preserving order).
- **Pattern:** `Hash Map / Bi-directional Mapping`
- **Recognition:** Need a one-to-one character mapping between two strings (bijection).
- **Key Insight:**
  - A valid mapping must be consistent in both directions:
    - `s → t`
    - `t → s`
  - If either mapping conflicts at any point, the strings are not isomorphic.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (since there are at most 256 ASCII characters or 26 lowercase letters)

### Example

```text
Input:
s = "egg"
t = "add"

Mapping:
e → a
g → d

Both directions are consistent → True
```

```text
Input:
s = "foo"
t = "bar"

f → b
o → a (first time), but later o → r (conflict)

Output:
False
```

## 0217 - Contains Duplicate

- **Problem:** Given an integer array `nums`, return `True` if any value appears at least twice in the array, otherwise return `False`.
- **Pattern:** `Hash Set / Hash Map`
- **Recognition:** Need to detect repeated elements efficiently while iterating.
- **Key Insight:**
  - A duplicate exists if an element is seen more than once during traversal.
  - Either track seen elements in a hash set/map or compare sizes after removing duplicates.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
nums = [1, 2, 3, 1]

Traversal:
1 → seen
2 → seen
3 → seen
1 → already seen → duplicate found

Output:
True
```

---

### Alternative Approach

```python
return len(nums) != len(set(nums))
```

- Converts array to a set (removes duplicates)
- If sizes differ → duplicates exist

## 0242 - Valid Anagram

- **Problem:** Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, otherwise return `False`.
- **Pattern:** `Frequency Counting (Hash Map)`
- **Recognition:** Need to compare character frequencies between two strings.
- **Key Insight:**
  - Two strings are anagrams if and only if they have identical character counts.
  - Count characters from one string and cancel them out using the second string.
  - Final verification ensures all counts return to zero.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (bounded alphabet) / `O(n)` (general case)

### Example

```text
Input:
s = "anagram"
t = "nagaram"

Frequency build:
a: 3, n: 1, g: 1, r: 1, m: 1

After processing t:
all counts return to 0 → True
```

---

### Key Implementation Idea

```python
return all(v == 0 for v in my_dict_letter_to_word.values())
```

- Ensures no leftover unmatched characters exist

## 0290 - Word Pattern

- **Problem:** Given a pattern string and a space-separated string `s`, determine if `s` follows the same pattern.
- **Pattern:** `Hash Map / Bi-directional Mapping`
- **Recognition:**
  - Need a one-to-one correspondence between two sequences
  - Similar to **Isomorphic Strings**
  - Mapping must be consistent in both directions
- **Key Insight:**
  - Maintain two hash maps:
    - `pattern character → word`
    - `word → pattern character`
  - For each position:
    - verify existing mappings are consistent
    - create new mappings if absent
  - Both mappings must agree to satisfy a bijection
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
pattern = "abba"
s = "dog cat cat dog"

Mappings:
a → dog
b → cat

Reverse Mappings:
dog → a
cat → b

All mappings consistent

Output:
True
```

```
Input:
pattern = "abba"
s = "dog cat cat fish"

Expected:
b → cat

Found:
b → fish

Conflict

Output:
False
```


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

## 0392 - Is Subsequence

- **Problem:** Given two strings `s` and `t`, return `True` if `s` is a subsequence of `t`, otherwise return `False`.
- **Pattern:** `Two Pointers`
- **Recognition:** Need to verify ordered matching of characters while scanning a larger string.
- **Key Insight:**
  - Traverse both strings using two pointers.
  - Advance the subsequence pointer only when characters match.
  - If all characters in `s` are matched in order, it is a valid subsequence.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
s = "abc"
t = "ahbgdc"

Matching process:
a → match
b → match
c → match

All characters found in order → True
```

```text
Input:
s = "axc"
t = "ahbgdc"

a → match
x → not found in order
c → not matched

Output:
False
```

## 0448 - Find All Numbers Disappeared in an Array

- **Problem:** Given an array containing numbers in the range `[1, n]`, find all numbers that do not appear in the array.
- **Pattern:** `Array Marking` / `Index Hashing`
- **Recognition:**
  - Values are constrained to `[1, n]`
  - Array indices can be reused as markers
  - Need `O(1)` extra space without hash sets
- **Key Insight:**
  - Treat each value as an index:

  - Mark presence by making the value at that index negative
  - After traversal:
    - positive indices represent missing numbers

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
  - excluding output array

### Example

```text
Input:
nums = [4,3,2,7,8,2,3,1]

Mark visited indices:
4 → mark index 3
3 → mark index 2
2 → mark index 1
7 → mark index 6
...
After marking:
[-4, -3, -2, -7, 8, 2, -3, -1]
```

## 0485 - Max Consecutive Ones

- **Problem:** Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.
- **Pattern:** `Linear Scan / Sliding Window (implicit)`
- **Recognition:** Need to track continuous streaks while resetting on breaks.
- **Key Insight:**
  - Maintain a running count of consecutive `1`s.
  - Reset the count whenever a `0` is encountered.
  - Keep track of the maximum streak seen so far.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [1,1,0,1,1,1]

Traversal:
1 → streak = 1
1 → streak = 2
0 → reset
1 → streak = 1
1 → streak = 2
1 → streak = 3

Output:
3
```

## 0496 - Next Greater Element I

- **Problem:** For each element in `nums1`, find the first greater element to its right in `nums2`. If none exists, return `-1`.
- **Pattern:** `Monotonic Stack`
- **Recognition:**
  - Need "next greater/smaller element"
  - Searching toward left/right for first larger value
  - Brute force involves nested loops → `O(n²)`
- **Key Insight:**
  - Use a decreasing monotonic stack to track unresolved elements
  - When current number is greater than stack top:
    - current number becomes the "next greater" for popped elements
  - Precompute mappings for all elements in `nums2`, then answer `nums1` queries in `O(1)`
- **Time Complexity:**
  - Current brute force solution: `O(n²)`
  - Optimal monotonic stack solution: `O(n)`
- **Space Complexity:** `O(n)`

### Example

````text
Input:
nums1 = [4,1,2]
nums2 = [1,3,4,2]

Mappings:
1 → 3
3 → 4
4 → -1
2 → -1

Output:
[-1,3,-1]

## 0605 - Can Place Flowers

- **Problem:** Given a flowerbed (array of 0s and 1s), determine if `n` new flowers can be planted without violating the rule that no two flowers can be adjacent.
- **Pattern:** `Greedy / Array Scanning`
- **Recognition:** Need to make locally optimal placements while respecting adjacency constraints.
- **Key Insight:**
  - A flower can be planted only if the current plot and both adjacent plots are empty.
  - Greedily place a flower whenever a valid position is found.
  - Each placement reduces future constraints immediately.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` (can be optimized to `O(1)`)

### Example

```text
Input:
flowerbed = [1,0,0,0,1], n = 1

Check positions:
Index 1 → cannot plant (left occupied)
Index 2 → can plant → place flower
Result:
[1,0,1,0,1]

Output:
True
````

---

### Note

- Padding with `0` simplifies boundary handling.
- This allows uniform checking for all indices without edge-case logic.

## 0605 - Can Place Flowers

- **Problem:** Determine if `n` new flowers can be planted in a flowerbed without violating the rule that no two adjacent plots can both contain flowers.
- **Pattern:** `Greedy`
- **Recognition:**
  - Need to make locally optimal placement decisions
  - Each placement affects neighboring positions
  - Goal is maximizing valid placements while scanning once
- **Key Insight:**
  - A flower can be planted only if:

  :contentReference[oaicite:0]{index=0}
  - Padding the array with zeros:

  ```text
  [0, *flowerbed, 0]
  ```

## 0724 - Find Pivot Index

- **Problem:** Find the pivot index where:
  - sum of elements to the left
  - equals sum of elements to the right
- **Pattern:** `Prefix Sum`
- **Recognition:**
  - Repeated left/right subarray sum comparisons
  - Need efficient running sum computation
  - Brute force nested summation would be `O(n²)`
- **Key Insight:**
  - Total array sum is known upfront
  - While traversing:

  :contentReference[oaicite:0]{index=0}
  - If:

  :contentReference[oaicite:1]{index=1}

  then current index is the pivot

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [1,7,3,6,5,6]

Index 0:
left = 0
right = 27

Index 1:
left = 1
right = 20

Index 3:
left = 11
right = 11

Output:
3
```

## 0896 - Monotonic Array

- **Problem:** Determine whether an array is monotonic, meaning it is entirely non-decreasing or non-increasing.
- **Pattern:** `Array Traversal`
- **Recognition:**
  - Need to identify whether the array changes in only one direction.
  - Equal adjacent elements are allowed.
  - A single pass is sufficient.
- **Key Insight:**
  - Traverse the array and track whether:
    - An increasing pair has been seen.
    - A decreasing pair has been seen.
  - If both increasing and decreasing pairs exist, the array is not monotonic.
  - Otherwise, it is either non-decreasing or non-increasing.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [1, 2, 2, 3]

Increasing pairs: Yes
Decreasing pairs: No

Output:
True
```

## 0929 - Unique Email Addresses

- **Problem:** Given a list of email addresses, return the number of unique emails after applying normalization rules.
- **Pattern:** `String Manipulation / Hash Set`
- **Recognition:** Need to transform each string into a canonical form and count distinct results.
- **Key Insight:**
  - Normalize each email before storing:
    - Ignore everything after `+` in local name.
    - Remove all `.` in local name.
    - Keep domain unchanged.
  - Use a set to automatically handle uniqueness.
- **Time Complexity:** `O(n * m)`
  - `n` = number of emails
  - `m` = average email length
- **Space Complexity:** `O(n)`

---

### Example

```text
Input:
["test.email+spam@leetcode.com",
 "testemail@leetcode.com"]

Normalization:

test.email+spam → testemail
testemail → testemail

Both become:
testemail@leetcode.com

Output:
1
```

---

### Key Implementation Insight

#### Clean approach (preferred)

```python
local, domain = email.split("@")
local = local.split("+")[0]
local = local.replace(".", "")
unique.add(f"{local}@{domain}")
```

- Uses built-in string operations instead of manual parsing
- More readable and less error-prone

---

### Note on Approaches

- Your first version:  
  ✔ good pointer-based parsing practice  
  ❌ more complex than necessary in Python

- Second version:  
  ⭐ preferred Pythonic solution  
  ✔ clean, readable, interview-ready

## 1002 - Find Common Characters

- **Problem:** Return all characters that appear in every string, including duplicates.
- **Pattern:** `Hash Map` / `Frequency Counting`
- **Recognition:**
  - Need the frequency of each character in every word.
  - A character is common only if it appears in all words.
  - The number of times it appears in the answer is the minimum frequency across all words.
- **Key Insight:**
  - Build a frequency map for each word.
  - For every character in the first word:
    - Check whether it exists in every other frequency map.
    - Track its minimum frequency across all words.
  - Add each common character to the result as many times as its minimum frequency.

- **Time Complexity:** `O(n × m)`
  - `n` = number of words
  - `m` = average length of a word
- **Space Complexity:** `O(n × k)`
  - `k` = number of distinct characters per word

### Example

```text
Input:
words = ["bella", "label", "roller"]

Frequencies:
l -> min(2, 2, 2) = 2
e -> min(1, 1, 1) = 1

Common characters:
["e", "l", "l"]

Output:
["e", "l", "l"]
```

## 1189 - Maximum Number of Balloons

- **Problem:** Determine how many instances of the word `"balloon"` can be formed using the characters in a string.
- **Pattern:** `Hash Map / Frequency Counting`
- **Recognition:**
  - Need character availability tracking
  - Problem involves forming a target word from given characters
  - Repeated character requirements matter (`l`, `o`)
- **Key Insight:**
  - Count frequencies of all characters in the input
  - The limiting character determines maximum `"balloon"` formations
  - Since:

  :contentReference[oaicite:0]{index=0}

  divide counts of:
  - `l` by `2`
  - `o` by `2`

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
  - fixed alphabet size

### Example

```text
Input:
text = "loonbalxballpoon"

Character Counts:
b → 2
a → 2
l → 4
o → 4
n → 2

Possible balloons:
min(2,2,4/2,4/2,2) = 2

Output:
2
```

## 1299 - Replace Elements with Greatest Element on Right Side

- **Problem:** Replace each element in the array with the greatest element among the elements to its right. The last element is replaced with `-1`.
- **Pattern:** `Reverse Traversal / Suffix Maximum`
- **Recognition:** Need to compute a running maximum from the right side of the array.
- **Key Insight:**
  - Traverse the array from right to left.
  - At each step, maintain the maximum value seen so far.
  - Replace current element with that running maximum.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` (can be optimized to `O(1)` in-place)

---

### Example

```text
Input:
arr = [17, 18, 5, 4, 6, 1]

Traversal from right:

Start: max = -1

1 → replace with -1 → max = 1
6 → replace with 1  → max = 6
4 → replace with 6  → max = 6
5 → replace with 6  → max = 6
18 → replace with 6 → max = 18
17 → replace with 18

Output:
[18, 18, 6, 6, 6, -1]
```

---

### Note

Your current solution uses an auxiliary array:

```python
result[j] = max(arr[j+1], result[j+1])
```

This works, but can be optimized to O(1) space by tracking a single `max_right` variable while traversing backward.

## 1394 - Find Lucky Integer in an Array

- **Problem:** A lucky integer is an integer whose value is equal to its frequency in the array. Return the largest such integer, or `-1` if none exist.
- **Pattern:** `Hash Map / Frequency Counting`
- **Recognition:**
  - Compare element values with their occurrence counts
  - Requires frequency tracking + conditional filtering
  - Need to maximize over valid candidates
- **Key Insight:**
  - Build frequency map of all elements
  - Check condition:

  k == frequency(k)
  - Track the largest valid lucky number

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
arr = [2,2,3,4]

Frequencies:
2 → 2
3 → 1
4 → 1

Valid lucky integers:
2

Output:
2
```

## 1408 - String Matching in an Array

- **Problem:** Given an array of words, return all strings that are substrings of another word in the array.
- **Pattern:** `Brute Force + String Search`
- **Recognition:** Need to check if any word exists inside another word in the list.
- **Key Insight:**
  - Compare each pair of words.
  - Only check containment (`in`) against the longer string to reduce unnecessary checks.
  - Store matches in a set to avoid duplicates.
- **Time Complexity:** `O(n² * m)`
  - `n` = number of words
  - `m` = average string length
- **Space Complexity:** `O(k)`
  - `k` = number of matching substrings

---

### Example

```text
Input:
["mass", "as", "hero", "superhero"]

Checks:
"as" is in "mass" → match
"hero" is in "superhero" → match

Output:
["as", "hero"]
```

---

### Key Insight (Important)

- Always compare smaller string inside larger string:
  ```python
  if small in large:
  ```
- This reduces unnecessary checks and improves clarity.

---

## 1436 - Destination City

- **Problem:** Given a list of directed paths, find the destination city that has no outgoing path.
- **Pattern:** `Hash Set`
- **Recognition:**
  - Need to identify a node that never appears as a source.
  - Fast membership checks are required.
  - A hash set efficiently stores all source cities.
- **Key Insight:**
  - Add every source city to a set.
  - Traverse the paths again.
  - The first destination city not present in the source set is the final destination.
  - Return that city.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
paths = [["A","B"], ["B","C"], ["C","D"]]

Source cities:
{A, B, C}

Destination cities:
B ✓
C ✓
D ✗

Output:
"D"
```

## 1684 - Count the Number of Consistent Strings

- **Problem:** Count how many strings consist only of characters from the given `allowed` string.
- **Pattern:** `Hash Set` / `String Traversal`
- **Recognition:**
  - Every character of a word must satisfy a membership condition.
  - If any character is not allowed, the word is invalid.
  - Each word can be checked independently.
- **Key Insight:**
  - Traverse each word character by character.
  - If any character is not in `allowed`, discard the word.
  - Otherwise, count it as a consistent string.

- **Time Complexity:** `O(n × m)`
  - `n` = number of words
  - `m` = average word length
- **Space Complexity:** `O(1)`

### Example

```text
Input:
allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]

Consistent:
"aaab"
"baa"

Output:
2
```

## 1752 - Check if Array Is Sorted and Rotated

- **Problem:** Determine whether an array is a sorted array that has been rotated some number of times.
- **Pattern:** `Array Traversal`
- **Recognition:**
  - A sorted array has no decreasing adjacent pairs.
  - A rotated sorted array has exactly one "drop" where the order decreases.
  - Comparing adjacent elements, including the last and first, is sufficient.
- **Key Insight:**
  - Traverse the array and count the number of positions where:
    ```text
    nums[i + 1] < nums[i]
    ```
  - Start from index `-1` so the comparison includes the last and first elements.
  - If there is more than one decreasing pair, the array cannot be a sorted rotated array.
  - Otherwise, return `True`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [3, 4, 5, 1, 2]

Drops:
5 > 1 ✓
All other adjacent pairs are non-decreasing.

Number of drops:
1

Output:
True
```


## 1800 - Maximum Ascending Subarray Sum

- **Problem:** Find the maximum possible sum of a strictly ascending contiguous subarray.
- **Pattern:** `Sliding Window` / `Kadane-Style Traversal`
- **Recognition:**
  - Need optimal contiguous subarray
  - Current state depends on previous adjacent comparison
  - Sequence either:
    - extends current window
    - or starts a new one
- **Key Insight:**
  - Maintain running ascending subarray sum:
    - if current number is larger than previous → extend subarray
    - otherwise → start new ascending subarray
  - Track global maximum during traversal
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [10,20,30,5,10,50]

Ascending Runs:
10 + 20 + 30 = 60
5 + 10 + 50 = 65

Output:
65
```

## 2053 - Kth Distinct String in an Array

- **Problem:** Return the `k`th distinct string in the array while preserving original order.  
  A distinct string appears exactly once.
- **Pattern:** `Hash Map / Frequency Counting`
- **Recognition:**
  - Need occurrence counting
  - Order of appearance matters
  - "Distinct" means frequency exactly `1`
- **Key Insight:**
  - First pass:
    - count frequencies of all strings
  - Second pass:
    - traverse original array order
    - decrement `k` only for distinct strings
  - When `k == 0`, current string is the answer
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
arr = ["d","b","c","b","c","a"]
k = 2

Frequencies:
d → 1
b → 2
c → 2
a → 1

Distinct strings in order:
["d","a"]

2nd distinct:
"a"

Output:
"a"
```

## 2206 - Divide Array Into Equal Pairs

- **Problem:** Determine whether the array can be divided into pairs such that both elements in each pair are equal.
- **Pattern:** `Hash Set`
- **Recognition:**
  - Every value must appear an even number of times.
  - Need to track whether an element has been seen an odd or even number of times.
  - A hash set can represent the parity of occurrences.
- **Key Insight:**
  - Traverse the array once.
  - For each number:
    - If it is already in the set, remove it.
    - Otherwise, add it to the set.
  - After processing all elements:
    - Numbers with even occurrences have been removed.
    - Numbers with odd occurrences remain.
  - The array can be divided into equal pairs only if the set is empty.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

### Example

```text
Input:
nums = [3, 2, 3, 2, 2, 2]

Set updates:
{3} → {3,2} → {2} → {} → {2} → {}

Set is empty.

Output:
True
```

## 2490 - Circular Sentence

- **Problem:** Determine whether a sentence is circular, where the first character of each word matches the last character of the previous word, and the first word also follows the last word.
- **Pattern:** `String Traversal`
- **Recognition:**
  - Need to compare adjacent words.
  - The comparison wraps around from the last word to the first.
  - Every pair must satisfy the same condition.
- **Key Insight:**
  - Split the sentence into words.
  - For each word, compare:
    - its first character
    - the last character of the previous word
  - Using `i - 1` naturally wraps the first word to the last.
  - If all comparisons match, the sentence is circular.

- **Time Complexity:** `O(n)`
  - `n` = length of the sentence
- **Space Complexity:** `O(w)`
  - `w` = number of words (due to splitting)

### Example

```text
Input:
sentence = "leetcode exercises sound delightful"

Comparisons:
e == e ✓
s == s ✓
d == d ✓
l == l ✓

Output:
True
```

## 2678 - Number of Senior Citizens

- **Problem:** Given a list of encoded passenger details, count how many passengers are older than 60.
- **Pattern:** `String Parsing + Filtering`
- **Recognition:** Need to extract a fixed-position substring and apply a numeric condition to each element.
- **Key Insight:**
  - Age is stored at a fixed index slice (`[11:13]`).
  - Convert substring to integer and apply condition.
  - Count how many elements satisfy the condition.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (optimal version) / `O(n)` (list comprehension version)

---

### Example

```text
Input:
details = ["1234567890AA61Z", "1234567890BB45Z"]

Extracted ages:
61 → senior
45 → not senior

Output:
1
```

---

### Approaches

#### 1. List comprehension (your version)

```python
return len([
    int(p[11:13])
    for p in details
    if int(p[11:13]) > 60
])
```

- Creates an intermediate list
- Less memory efficient

---

#### 2. Optimized (recommended)

```python
return sum(int(p[11:13]) > 60 for p in details)
```

- No intermediate list created
- `True = 1`, `False = 0`
- More Pythonic and efficient

---

### Key Insight

👉 Prefer `sum(condition)` over `len([condition])` when you are counting matches.

This avoids unnecessary memory allocation and is the standard interview-ready approach.

## 2965 - Find Missing and Repeated Values

- **Problem:** In an `n x n` grid containing numbers from `1` to `n²`:
  - one number appears twice
  - one number is missing
    return `[repeated, missing]`
- **Pattern:** `Hash Set`
- **Recognition:**
  - Need duplicate + missing detection
  - Values belong to a fixed known range
  - Membership lookup/removal needed efficiently
- **Key Insight:**
  - Initialize a set containing all expected values:

  :contentReference[oaicite:0]{index=0}
  - Traverse grid:
    - first occurrence → remove from set
    - second occurrence → repeated value found
  - Remaining value in set is the missing number

- **Time Complexity:** `O(n²)`
- **Space Complexity:** `O(n²)`

### Example

```text
Input:
grid = [
  [1,3],
  [2,2]
]

Expected values:
{1,2,3,4}

Traversal:
1 → remove
3 → remove
2 → remove
2 → duplicate found

Remaining:
4

Output:
[2,4]
```

## 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray

- **Problem:** Find the length of the longest contiguous subarray that is either:
  - strictly increasing
  - or strictly decreasing
- **Pattern:** `Sliding Window` / `Sequential Traversal`
- **Recognition:**
  - Need longest continuous streak/subarray
  - Adjacent element comparison drives state changes
  - Only local neighboring relationships matter
- **Key Insight:**
  - Track two running lengths:
    - `inc` → current increasing streak
    - `dec` → current decreasing streak
  - For each adjacent pair:
    - increasing → extend `inc`, reset `dec`
    - decreasing → extend `dec`, reset `inc`
    - equal → reset both
  - Maintain global maximum throughout traversal
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [1,4,3,3,2]

Traversal:
1 → 4   increasing (inc = 2)
4 → 3   decreasing (dec = 2)
3 → 3   reset
3 → 2   decreasing (dec = 2)

Longest monotonic length:
2
```

## 3110 - Score of a String

- **Problem:** Given a string `s`, compute the sum of absolute differences between ASCII values of all adjacent characters.
- **Pattern:** `Linear Scan / Pairwise Computation`
- **Recognition:** Need to compare adjacent characters in sequence.
- **Key Insight:**
  - Iterate through the string and consider each adjacent pair.
  - Convert characters to ASCII using `ord()`.
  - Sum absolute differences for each pair.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

### Example

```text
Input:
s = "hello"

Pairs:
h-e → |104 - 101| = 3
e-l → |101 - 108| = 7
l-l → |108 - 108| = 0
l-o → |108 - 111| = 3

Output:
13
```

---

### Key Insight

- Only adjacent comparisons matter.
- No need for extra data structures.
- Direct accumulation is optimal.

## 3151 - Special Array I

- **Problem:** Determine whether an array is special, where every pair of adjacent elements has opposite parity.
- **Pattern:** `Array Traversal`
- **Recognition:**
  - Only adjacent elements need to be compared.
  - A valid array alternates between even and odd numbers.
  - A single violation makes the array invalid.
- **Key Insight:**
  - Traverse the array once.
  - For each adjacent pair, compare their parity using:
    ```text
    nums[i] % 2
    ```
  - If two consecutive elements have the same parity, return `False`.
  - If all adjacent pairs have opposite parity, return `True`.

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

### Example

```text
Input:
nums = [2, 1, 4, 3]

Parity:
Even → Odd → Even → Odd

Output:
True
```

## 3442 - Maximum Difference Between Even and Odd Frequency

- **Problem:** Find the maximum difference between:
  - the highest odd character frequency
  - and the smallest even character frequency
- **Pattern:** `Hash Map / Frequency Counting`
- **Recognition:**
  - Need character occurrence tracking
  - Problem involves frequency-based conditions (`odd/even`)
  - Single-pass counting followed by aggregation/min-max evaluation
- **Key Insight:**
  - Count all character frequencies using a hash map
  - Track:
    - largest odd frequency
    - smallest even frequency
  - Final answer:
    - If no odd frequencies → return 0
    - If no even frequencies → return largest odd frequency
    - Otherwise → return `largest_odd - smallest_even`

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
  - At most fixed alphabet size (e.g. lowercase English letters)

### Example

```text
Input:
s = "aaaaabbc"

Frequencies:
a → 5 (odd)
b → 2 (even)
c → 1 (odd)

odd_max = 5
even_min = 2

Output:
3
```
