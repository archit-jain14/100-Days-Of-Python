# Day 92: Function Caching in Python ⚡💾

## 📌 Overview
Welcome to **Day 92** of the 100 Days of Code challenge! Today, we explored **Function Caching** in Python using the **`functools.lru_cache`** decorator. Function Caching is an optimization technique used to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.

---

## 💻 Key Concepts Covered Today

### 1. What is Function Caching & `lru_cache`?
*   **Least Recently Used (LRU) Cache:** A caching strategy that discards the least recently used items first when the cache size limit is reached.
*   **Decorator:** `@lru_cache(maxsize=None)` memoizes function call outputs for specified parameters, skipping repetitive costly computations.

### 2. When to Use Function Caching?
*   For **deterministic/pure functions** where the same inputs always produce the exact same output.
*   For computationally expensive tasks (e.g., recursive Fibonacci, heavy mathematical processing, database/API fetch caching).

---

## 🛠️ Code Snippet Example

```python
import time
from functools import lru_cache

# Caching function execution results
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)  # Simulating a heavy calculation
    return n * 5

# First calls take 5 seconds each
print(fx(20))  # Takes 5 seconds
print("done for 20")

print(fx(2))   # Takes 5 seconds
print("done for 2")

# Repeated calls run instantly from cache!
print(fx(20))  # Instant result from cache!
print("done for 20")

print(fx(2))   # Instant result from cache!
print("done for 2")
