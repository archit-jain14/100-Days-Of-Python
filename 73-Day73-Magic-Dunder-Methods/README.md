# Day 73: Magic/Dunder Methods in Python 🪄

## 📌 Overview
Welcome to **Day 73** of the 100 Days of Code challenge! Today, we explored **Magic Methods** (also known as **Dunder Methods** because they start and end with double underscores `__`). These special predefined methods allow us to emulate built-in behavior in custom classes, customize object initialization, string representation, operator overloading, and length determination.

---

## 💻 Key Concepts Covered Today

### 1. What are Magic/Dunder Methods?
*   Special built-in methods in Python that are automatically invoked in response to specific operations.
*   Examples: `__init__` for initialization, `__len__` for `len()`, `__str__` for standard string representation, and `__repr__` for developer debugging representation.

### 2. Common Dunder Methods
*   `__init__()`: Called automatically when an object is created.
*   `__str__()`: Defines a readable, user-friendly string representation of an object (called by `print()` or `str()`).
*   `__repr__()`: Defines an unambiguous string representation for developers/debugging (called by `repr()`).
*   `__len__()`: Returns the length of an object when `len(obj)` is executed.
*   `__call__()`: Allows an instance of a class to be called as if it were a function `obj()`.

---

## 🛠️ Code Snippet Example

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __len__(self):
        # Returns the number of characters in employee's name
        return len(self.name)

    def __str__(self):
        # User-friendly string display
        return f"Employee Name: {self.name}"

    def __repr__(self):
        # Official developer representation
        return f"Employee('{self.name}', {self.salary})"

    def __call__(self):
        print(f"Employee {self.name} is actively working.")

# Creating Object
e = Employee("Archit", 95000)

print(str(e))   # Output: Employee Name: Archit
print(repr(e))  # Output: Employee('Archit', 95000)
print(len(e))   # Output: 6
e()             # Output: Employee Archit is actively working.
