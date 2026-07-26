# Day 65: Static Methods in Python ⚡

## 📌 Overview
Welcome to **Day 65** of the 100 Days of Code challenge! Today, we explored **Static Methods** in Python OOPs. Static methods are methods that belong to a class rather than an instance of the class. They don't require access to instance-specific data (`self`) or class-specific data (`cls`), making them ideal for self-contained utility functions.

---

## 💻 Key Concepts Covered Today

### 1. What is a Static Method?
*   A method bound to the class rather than the object of the class.
*   Defined using the `@staticmethod` decorator.
*   Does **not** take `self` or `cls` as an implicit first parameter.

### 2. When to use Static Methods?
*   When you have a utility function that performs a task in isolation from class attributes or instance state.
*   Helps organize helper functions logically within a class structure.

---

## 🛠️ Code Snippet Example

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Calling static methods directly using the Class Name (No object instantiation needed!)
result_sum = MathUtils.add(15, 25)
print(f"Sum: {result_sum}")  # Outputs: Sum: 40

check_even = MathUtils.is_even(10)
print(f"Is 10 even? {check_even}")  # Outputs: Is 10 even? True

# Can also be called via an instance
obj = MathUtils()
print(obj.add(5, 5))  # Outputs: 10
