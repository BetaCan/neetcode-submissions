class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))




"""

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

## What the code is doing
It checks whether the array contains any repeated values.

The key idea is:

- `len(nums)` = total number of elements in the original array
- `len(set(nums))` = number of **unique** elements

If those two numbers are different, then some value must have appeared more than once.

---

## Step by step

### 1. `class Solution:`
This is just a container for the function.  
Many coding platforms expect your solution inside a class named `Solution`.

---

### 2. `def hasDuplicate(self, nums: List[int]) -> bool:`
This defines a function:

- `nums` is the input list of integers
- `-> bool` means the function returns either `True` or `False`

---

### 3. `set(nums)`
A `set` in Python stores only **unique** values.

Example:

```python
nums = [1, 2, 3, 3]
set(nums)  # {1, 2, 3}
```

Notice the second `3` is removed because sets do not allow duplicates.

---

### 4. `len(nums)`
This counts all elements in the original list.

For:

```python
nums = [1, 2, 3, 3]
```

`len(nums) = 4`

---

### 5. `len(set(nums))`
This counts how many unique numbers are in the list.

For the same example:

```python
set(nums) = {1, 2, 3}
len(set(nums)) = 3
```

---

### 6. Comparison
```python
len(nums) != len(set(nums))
```

- If the lengths are different, there is at least one duplicate
- If the lengths are the same, all values are unique

---

## Example walkthrough

### Example 1:
```python
nums = [1, 2, 3, 3]
```

- `len(nums) = 4`
- `set(nums) = {1, 2, 3}`
- `len(set(nums)) = 3`

Since `4 != 3`, the function returns `True`.

---

### Example 2:
```python
nums = [1, 2, 3, 4]
```

- `len(nums) = 4`
- `set(nums) = {1, 2, 3, 4}`
- `len(set(nums)) = 4`

Since `4 != 4` is `False`, the function returns `False`.

---

## Why this is efficient
This solution is very clean and fast:

- **Time complexity:** `O(n)`  
  because Python has to look through the list once to build the set

- **Space complexity:** `O(n)`  
  because the set may store all numbers if they are unique

---

## In plain English
This code says:

> “If the number of items in the array is not the same as the number of unique items, then there must be a duplicate.”

If you want, I can also show you:
1. the same logic using a loop and set, or  
2. a visual dry run with a small example.

"""
