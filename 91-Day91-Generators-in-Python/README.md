# Day 91: Generators in Python ⚡⚙️

## 📌 Overview
Welcome to **Day 91** of the 100 Days of Code challenge! Today, we explored **Generators** in Python. Generators are special functions that return an iterable generator object, allowing us to generate values on the fly (lazy evaluation) rather than computing and storing them in memory all at once.

---

## 💻 Key Concepts Covered Today

### 1. What are Generators?
*   Functions that use the **`yield`** statement instead of `return`.
*   When called, they do not execute immediately; instead, they return a generator object that produces items on demand using `next()` or inside loops.

### 2. Benefits of Generators
*   **Memory Efficiency:** Generates values dynamically one at a time, making it ideal for processing massive datasets or infinite sequences without running out of RAM.
*   **State Retention:** Automatically pauses execution and resumes right from where it left off on subsequent calls.

---

## 🛠️ Code Snippet Example

```python
# 1. Defining a Generator Function
def my_generator():
    for i in range(5):
        yield i

# 2. Consuming Generator using next()
gen = my_generator()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

# 3. Iterating through a Generator
print("\nIterating remaining values:")
for value in gen:
    print(value)
