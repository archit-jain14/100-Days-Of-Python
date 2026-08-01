# Day 80: Multilevel Inheritance in Python 🧬🪜

## 📌 Overview
Welcome to **Day 80** of the 100 Days of Code challenge! Today, we explored **Multilevel Inheritance** in Python Object-Oriented Programming. Multilevel Inheritance is a structure where a child class inherits from a parent class, which in turn inherits from another grandparent class forming a chain of inheritance (`BaseClass` ➔ `DerivedClass1` ➔ `DerivedClass2`).

---

## 💻 Key Concepts Covered Today

### 1. What is Multilevel Inheritance?
*   A transitive inheritance chain where attributes and methods cascade down from the topmost base class to the leaf child class.
*   The bottom-most class gets access to features of all its ancestor classes.

### 2. Constructor & Method Resolution
*   `super()` allows calling methods and constructors up the chain level by level.
*   Helps maintain a clean hierarchical structure without code duplication across multi-tiered entities.

---

## 🛠️ Code Snippet Example

```python
# Base / Grandparent Class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name} | Species: {self.species}")

# Parent Class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def show_details(self):
        super().show_details()
        print(f"Breed: {self.breed}")

# Child Class inheriting from Dog (Multilevel Chain)
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        super().__init__(name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        super().show_details()
        print(f"Color: {self.color}")

# Creating Object of the leaf class
dog = GoldenRetriever("Buddy", "Golden Yellow")
dog.show_details()
