# Day 81: Hybrid and Hierarchical Inheritance in Python 🧬🌳

## 📌 Overview
Welcome to **Day 81** of the 100 Days of Code challenge! Today, we explored **Hierarchical Inheritance** and **Hybrid Inheritance** in Python Object-Oriented Programming. These advanced inheritance patterns allow complex relationship modeling across multiple class structures while maintaining code modularity and clarity.

---

## 💻 Key Concepts Covered Today

### 1. Hierarchical Inheritance
*   Occurs when **multiple child classes inherit from a single parent class**.
*   **Structure:** Parent Class ➔ Child Class 1, Child Class 2, Child Class 3.
*   Enables sharing base functionality across different specialized classes.

### 2. Hybrid Inheritance
*   A combination of **two or more types of inheritance** (e.g., Single + Multiple + Hierarchical) within a single program.
*   Relies heavily on Python's **Method Resolution Order (MRO)** to avoid ambiguity (such as the Diamond Problem).

---

## 🛠️ Code Snippet Example

```python
# --- 1. Hierarchical Inheritance Example ---
class BaseDevice:
    def power_on(self):
        print("Device powered ON")

class Laptop(BaseDevice):
    def code(self):
        print("Coding on laptop...")

class Smartphone(BaseDevice):
    def make_call(self):
        print("Calling from smartphone...")


# --- 2. Hybrid Inheritance Example ---
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(f"{self.name} is studying.")

class Athlete:
    def train(self):
        print("Training in sports.")

# StudentAthlete inherits from Student (Single) and Athlete (Multiple) -> Hybrid Structure
class StudentAthlete(Student, Athlete):
    def __init__(self, name):
        super().__init__(name)

# Instantiating objects
sa = StudentAthlete("Archit")
sa.study()  # Inherited via Student -> Person
sa.train()  # Inherited via Athlete
