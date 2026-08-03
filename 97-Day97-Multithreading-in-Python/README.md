# Day 97: Multithreading in Python 🧵⚡

## 📌 Overview
Welcome to **Day 97** of the 100 Days of Code challenge! Today, we explored **Multithreading** in Python using the built-in **`threading`** module and **`concurrent.futures.ThreadPoolExecutor`**. Multithreading allows a program to run multiple threads concurrently, making it ideal for I/O-bound tasks such as network requests, file downloading, and reading/writing operations.

---

## 💻 Key Concepts Covered Today

### 1. What is Multithreading?
*   A thread is a lightweight unit of execution within a process.
*   Enables concurrent execution of tasks by switching execution between threads during I/O wait times.

### 2. Core Concepts & Methods
*   **`threading.Thread(target, args)`**: Creates a thread object to run a specific function.
*   **`t.start()`**: Starts the thread execution.
*   **`t.join()`**: Pauses the main program until the thread finishes execution.
*   **`ThreadPoolExecutor`**: Manages a pool of threads automatically using context managers (`with` block) and handles mapping or submitting tasks cleanly.

---

## 🛠️ Code Snippet Example

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

# 1. Using threading Module Directly
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])

t1.start()
t2.start()

t1.join()
t2.join()

# 2. Using ThreadPoolExecutor
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(f"Completed: {result}")

poolingDemo()
