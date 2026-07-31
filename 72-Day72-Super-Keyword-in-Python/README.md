# Day 72: The `super()` Keyword in Python 🦸‍♂️

## 📌 Overview
Welcome to **Day 72** of the 100 Days of Code challenge! Today, we explored the **`super()`** keyword in Python Object-Oriented Programming. The `super()` function is used to give access to methods and properties of a parent or sibling class. It allows us to invoke parent class methods without explicitly naming the parent class, promoting code reusability and maintaining dynamic inheritance structures.

---

## 💻 Key Concepts Covered Today

### 1. What is `super()`?
*   A built-in Python function that returns a proxy object delegating method calls to a parent or sibling class.
*   Most commonly used inside child class constructors (`__init__`) to invoke the parent class constructor and initialize inherited attributes.

### 2. Benefits of Using `super()`
*   **Reduces Code Redundancy:** Prevents duplicating initialization logic already defined in the parent class.
*   **Flexibility:** Makes code maintenance easier if the parent class name changes or during complex multiple inheritance scenarios.

---

## 🛠️ Code Snippet Example

```python
class ParentClass:
    def __init__(self, name):
        self.name = name

    def parent_method(self):
        print(f"Parent method called by {self.name}")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        # Calling parent constructor using super()
        super().__init__(name)
        self.age = age

    def child_method(self):
        # Calling parent method using super()
        super().parent_method()
        print(f"Child age is {self.age}")

# Creating Object
child_obj = ChildClass("Archit", 22)
child_obj.child_method()
