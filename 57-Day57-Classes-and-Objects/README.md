# Day 57: Deep Dive into Classes and Objects in Python 🏗️

## 📌 Overview
Welcome to **Day 57** of the 100 Days of Code challenge! Today, we took a deeper look into **Classes and Objects** in Python. We explored how to model real-world entities, manage object attributes dynamically, and understood the crucial role of the `self` parameter when invoking methods within a class.

---

## 💻 Key Concepts Covered Today

### 1. Class Attributes vs Instance Attributes
*   **Class Attributes:** Shared by all instances (objects) of the class. Defined directly inside the class body.
*   **Instance Attributes:** Specific to a particular object. They can be created dynamically or initialized specifically for an individual instance.

### 2. The Role of the `self` Parameter
*   `self` represents the instance of the class that is currently calling the method.
*   It allows each object to access its own attributes and methods. 
*   When you call `object.method()`, Python automatically translates it under the hood to `Class.method(object)`.

---

## 🛠️ Code Snippet Example

```python
class Person:
    # Class Attribute (Same for everyone)
    species = "Human"

    # Method utilizing the 'self' parameter
    def introduce(self):
        print(f"Hi, I am {self.name} and I work as a {self.occupation}.")

# Creating individual objects
person1 = Person()
person1.name = "Archit"
person1.occupation = "Software Engineer"

person2 = Person()
person2.name = "Rohan"
person2.occupation = "Data Scientist"

# Calling the method (self automatically passes person1 and person2 respectively)
person1.introduce()  # Outputs: Hi, I am Archit and I work as a Software Engineer.
person2.introduce()  # Outputs: Hi, I am Rohan and I work as a Data Scientist.
