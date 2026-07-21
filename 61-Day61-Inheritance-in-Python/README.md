# Day 61: Inheritance in Python 🧬

## 📌 Overview
Welcome to **Day 61** of the 100 Days of Code challenge! Today, we explored **Inheritance**, one of the fundamental concepts of Object-Oriented Programming (OOPs) in Python. Inheritance allows a child class to inherit attributes and methods from a parent class, promoting code reusability, reducing redundancy, and maintaining a clear hierarchy in application design.

---

## 💻 Key Concepts Covered Today

### 1. What is Inheritance?
*   The mechanism by which one class (derived or child class) inherits the properties and behaviors (methods) of another class (base or parent class).
*   **Syntax:** `class ChildClass(ParentClass):`

### 2. Advantages of Inheritance
*   **Reusability:** Write code once in the parent class and reuse it across multiple child classes.
*   **Extensibility:** Modify or add new features in the child class without modifying the existing parent class code.

---

## 🛠️ Code Snippet Example

```python
# Parent Class (Base Class)
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def show_details(self):
        print(f"Employee ID: {self.id} | Name: {self.name}")

# Child Class (Derived Class inheriting from Employee)
class Programmer(Employee):
    def __init__(self, name, emp_id, language):
        # Accessing parent attributes or extending features
        super().__init__(name, emp_id)
        self.language = language

    def show_language(self):
        print(f"{self.name} programs in {self.language}.")

# Instantiating Child Class
p1 = Programmer("Archit", 401, "Python")

# Accessing methods from both parent and child classes
p1.show_details()   # Inherited from Employee
p1.show_language()  # Specific to Programmer
