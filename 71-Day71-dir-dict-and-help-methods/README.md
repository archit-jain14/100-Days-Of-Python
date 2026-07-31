# Day 71: `dir()`, `__dict__`, and `help()` in Python 🔍

## 📌 Overview
Welcome to **Day 71** of the 100 Days of Code challenge! Today, we explored **Object Introspection** in Python using three fundamental built-in functions/attributes: `dir()`, `__dict__`, and `help()`. Object introspection allows developers to examine the properties, methods, and documentation of objects dynamically at runtime.

---

## 💻 Key Concepts Covered Today

### 1. `dir()` Method
*   Returns a sorted list of valid attributes and methods available for an object or class.
*   Extremely useful when exploring unfamiliar libraries or built-in types to see what functions are available.

### 2. `__dict__` Attribute
*   A dictionary/mapping that stores an object's writable attributes (instance attributes).
*   Provides a quick key-value view of all instance variables and their current values.

### 3. `help()` Function
*   Used to get detailed documentation and docstrings of any module, class, function, or object.
*   Gives full context on method signatures and parameter details.

---

## 🛠️ Code Snippet Example

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Archit", 22)

# 1. Using dir() to inspect available attributes/methods
print(dir(p1))

# 2. Using __dict__ to view instance attributes as a dictionary
print(p1.__dict__)
# Output: {'name': 'Archit', 'age': 22}

# 3. Using help() to read complete documentation
help(Person)
