# Day 53: Map, Filter, and Reduce in Python 🛠️

## 📌 Overview
Welcome to **Day 53** of the 100 Days of Code challenge! Today, we dived into three powerful built-in higher-order functions in Python: `map()`, `filter()`, and `reduce()`. These functions allow us to apply a specific function to a sequence of elements (like lists) in a clean, elegant, and functional programming style, often combined with Lambda functions.

---

## 💻 Key Concepts Covered Today

### 1. The `map()` Function
*   Applies a given function to all items in an iterable (list, tuple, etc.) and returns a map object (iterator).
*   **Syntax:** `map(function, iterable)`

### 2. The `filter()` Function
*   Filters elements from an iterable based on whether they meet a specific condition (i.e., the function returns `True`).
*   **Syntax:** `filter(function, iterable)`

### 3. The `reduce()` Function
*   Unlike `map` and `filter`, `reduce()` belongs to the `functools` module. 
*   It applies a function rolling-ly to sequential pairs of elements, reducing the entire iterable to a **single cumulative value**.
*   **Syntax:** `reduce(function, iterable)`

---

## 🛠️ Code Snippet Example

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 1. Map: Square each number
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Outputs: [1, 4, 9, 16, 25]

# 2. Filter: Get only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)    # Outputs: [2, 4]

# 3. Reduce: Calculate the sum of all numbers
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)  # Outputs: 15
