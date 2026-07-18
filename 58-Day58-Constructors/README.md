# Day 58: Constructors in Python 🏗️

## 📌 Overview
Welcome to **Day 58** of the 100 Days of Code challenge! Today, we explored **Constructors** in Python Object-Oriented Programming. Instead of manually assigning properties to every object after creation, constructors allow us to initialize an object's attributes automatically at the exact moment the object is instantiated.

---

## 💻 Key Concepts Covered Today

### 1. What is a Constructor?
*   A special method used to initialize or assign values to the data members of a class when an object is created.
*   In Python, the `__init__()` method is reserved to act as the constructor.
*   It is called automatically every time a new object of that class is instantiated.

### 2. Types of Constructors
*   **Parameterized Constructor:** Takes arguments from the user during object creation to dynamically assign custom values to instances.
*   **Default Constructor:** Takes no arguments except `self`. It initializes attributes with fixed or default values for every object.

---

## 🛠️ Code Snippet Example

```python
class Developer:
    # Parameterized Constructor
    def __init__(self, name, language):
        self.name = name
        self.language = language
        print(# Basic initialization log
            f"Constructor called automatically for {self.name}"
        )

    def display_info(self):
        print(f"{self.name} specializes in {self.language}.")

# Objects created and automatically initialized using the constructor
dev1 = Developer("Archit", "Python/Django")
dev2 = Developer("Rohan", "JavaScript")

# Accessing methods
dev1.display_info()  # Outputs: Archit specializes in Python/Django.
dev2.display_info()  # Outputs: Rohan specializes in JavaScript.
