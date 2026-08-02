# Day 84: Time Module in Python ⏰

## 📌 Overview
Welcome to **Day 84** of the 100 Days of Code challenge! Today, we explored the built-in **`time` module** in Python. The `time` module provides various functions for handling time-related tasks, benchmarking code performance, introducing delays, and formatting timestamps into human-readable date strings.

---

## 💻 Key Concepts Covered Today

### 1. Core Functions in `time` Module
*   **`time.time()`**: Returns the current time in seconds since the Epoch (January 1, 1970). Frequently used to measure script execution time.
*   **`time.sleep(seconds)`**: Pauses/delays execution of the program for the specified number of seconds.
*   **`time.strftime(format)`**: Formats a time tuple or `struct_time` into a readable string according to specified directives (e.g., `%Y-%m-%d %H:%M:%S`).
*   **`time.localtime()`**: Converts seconds since epoch into local time `struct_time`.

---

## 🛠️ Code Snippet Example

```python
import time

# 1. Measuring Code Execution Time
def using_while():
    i = 0
    while i < 50000:
        i += 1

init_time = time.time()
using_while()
execution_time = time.time() - init_time
print(f"Time taken by while loop: {execution_time:.4f} seconds")

# 2. Introducing Delay with time.sleep()
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Resumed execution!")

# 3. Formatting Time with time.strftime()
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(f"Formatted Local Time: {formatted_time}")
