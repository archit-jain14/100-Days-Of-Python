# Day 79: Multiple Inheritance in Python 🧬🔀

## 📌 Overview
Welcome to **Day 79** of the 100 Days of Code challenge! Today, we explored **Multiple Inheritance** in Python Object-Oriented Programming. Multiple Inheritance occurs when a child class derives attributes and methods from **more than one parent class**. We also looked into **Method Resolution Order (MRO)**, which dictates how Python resolves method calls in complex inheritance hierarchies.

---

## 💻 Key Concepts Covered Today

### 1. What is Multiple Inheritance?
*   A mechanism where a child class inherits properties from multiple base classes simultaneously.
*   **Syntax:** `class ChildClass(Parent1, Parent2):`

### 2. Method Resolution Order (MRO)
*   The order in which Python searches for attributes or methods in a class hierarchy.
*   Python uses the C3 Linearization algorithm to determine MRO.
*   You can inspect the MRO of any class using `ClassName.mro()` or `ClassName.__mro__`.

---

## 🛠️ Code Snippet Example

```python
# Base Class 1
class Employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Employee Name: {self.name}")

# Base Class 2
class Dancer:
    def __init__(self, dance_style):
        self.dance_style = dance_style

    def show_dance(self):
        print(f"Dance Style: {self.dance_style}")

# Derived Class inheriting from BOTH Employee and Dancer
class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance_style):
        Employee.__init__(self, name)
        Dancer.__init__(self, dance_style)

# Creating Object
obj = DancerEmployee("Archit", "Hip Hop")

obj.show_name()   # Inherited from Employee
obj.show_dance()  # Inherited from Dancer

# Checking Method Resolution Order (MRO)
print(DancerEmployee.mro())
