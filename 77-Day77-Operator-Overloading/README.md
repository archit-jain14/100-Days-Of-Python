# Day 77: Operator Overloading in Python ➕➖✖️

## 📌 Overview
Welcome to **Day 77** of the 100 Days of Code challenge! Today, we explored **Operator Overloading** in Python Object-Oriented Programming. Operator Overloading allows us to redefine or extend the behavior of built-in operators (such as `+`, `-`, `*`, `<`, etc.) for custom user-defined objects using special magic/dunder methods.

---

## 💻 Key Concepts Covered Today

### 1. What is Operator Overloading?
*   Giving extended meaning beyond predefined primitive data types to an existing operator.
*   For instance, using `+` to add two custom `Vector` or `ComplexNumber` objects directly.

### 2. Common Dunder Methods for Operators
*   `__add__(self, other)`: Overloads the addition `+` operator.
*   `__sub__(self, other)`: Overloads the subtraction `-` operator.
*   `__mul__(self, other)`: Overloads the multiplication `*` operator.
*   `__str__(self)`: Overloads string representation for `print()` calls.

---

## 🛠️ Code Snippet Example

```python
class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    # Operator Overloading for +
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

# Creating Vector Objects
v1 = Vector(3, 5, 6)
v2 = Vector(1, 2, 9)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")

# Using + operator directly on custom Vector objects
v3 = v1 + v2
print(f"Sum (v1 + v2): {v3}")
