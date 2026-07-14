# Day 54: 'is' vs '==' in Python 🐍

## 📌 Overview
Welcome to **Day 54** of the 100 Days of Code challenge! Today, we explored one of the most fundamental yet commonly confused topics in Python: the difference between the identity operator (`is`) and the equality operator (`==`). Understanding this is crucial for managing memory efficiency and avoiding subtle bugs in comparisons.

---

## 💻 Key Concepts Covered Today

### 1. The `==` (Equality) Operator
*   Compares the **values** of two objects.
*   It returns `True` if the contents/values of both objects are the same, regardless of where they are stored in memory.

### 2. The `is` (Identity) Operator
*   Compares the **memory location (identity)** of two objects using their unique ID (i.e., `id()`).
*   It returns `True` only if both variables point to the exact same object in memory.

### 3. Behavior with Immutable vs Mutable Objects
*   **Immutable Objects (Strings, Integers):** Python optimizes memory using *string interning* and *integer caching* (for numbers between -5 and 256). Thus, two variables with the same value often share the same memory location, making both `==` and `is` return `True`.
*   **Mutable Objects (Lists, Dictionaries):** Every time you create a new list or dictionary, Python allocates a fresh, unique memory address even if the values inside are identical. Therefore, `==` will be `True`, but `is` will be `False`.

---

## 🛠️ Code Snippet Example

```python
# Comparison with Immutable Objects (Integers)
a = 50
b = 50
print(a == b)  # True (Same value)
print(a is b)  # True (Same memory address due to integer caching)

# Comparison with Mutable Objects (Lists)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True (Same values)
print(list1 is list2)  # False (Different locations in memory)
