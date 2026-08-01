# Day 78: Single Inheritance in Python 🧬

## 📌 Overview
Welcome to **Day 78** of the 100 Days of Code challenge! Today, we explored **Single Inheritance** in Python Object-Oriented Programming. Single Inheritance is the simplest and most foundational form of inheritance where a single child class (derived class) inherits attributes and methods from a single parent class (base class).

---

## 💻 Key Concepts Covered Today

### 1. What is Single Inheritance?
*   A mechanism where a child class derives directly from **one** parent class.
*   Enables code reuse and allows extending or modifying the parent class functionality without altering the original base class code.

### 2. Syntax & Mechanics
*   **Syntax:** `class ChildClass(ParentClass):`
*   The child class gets access to all public and protected attributes and methods of the parent class.
*   `super()` can be used inside the child class to invoke parent class methods or constructors.

---

## 🛠️ Code Snippet Example

```python
# Base / Parent Class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

# Derived / Child Class (Single Inheritance)
class Dog(Animal):
    def __init__(self, name, breed):
        # Inheriting attributes from Animal class
        super().__init__(name, species="Dog")
        self.breed = breed

    # Extending functionality
    def make_sound(self):
        print("Bark! Bark!")

# Creating Object
d = Dog("Buddy", "Golden Retriever")
print(f"Name: {d.name} | Species: {d.species} | Breed: {d.breed}")
d.make_sound()  # Output: Bark! Bark!
