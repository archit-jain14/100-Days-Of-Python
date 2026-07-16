# Day 56: Introduction to OOPs (Object-Oriented Programming) in Python 🏢

## 📌 Overview
Welcome to **Day 56** of the 100 Days of Code challenge! Today marks the beginning of a major milestone: **Object-Oriented Programming (OOPs)**. Moving away from procedural programming, OOPs allows us to structure our code by mapping real-world entities into software structures using **Classes** and **Objects**, making our programs modular, reusable, and easy to maintain.

---

## 💻 Key Concepts Covered Today

### 1. What is OOPs?
*   A programming paradigm that uses **objects** to represent data and methods.
*   It aims to implement real-world entities like inheritance, polymorphism, encapsulation, etc., in programming.

### 2. Class vs Object
*   **Class:** A blueprint or template for creating objects. It defines the structure, attributes (properties), and behaviors (methods) that the objects will have.
*   **Object:** An instance of a class. When a class is defined, no memory is allocated until an object of that class is created.

---

## 🛠️ Code Snippet Example

```python
# Defining a Class
class RailwayForm:
    formType = "Railway Reservation Form"
    
    # Method/Behavior inside the class
    def printData(self):
        print(self.formType)
        print(f"Name: {self.name}")
        print(f"Train: {self.train}")

# Creating Objects (Instances of the Class)
harryApplication = RailwayForm()
harryApplication.name = "Harry"
harryApplication.train = "Rajdhani Express"

# Calling method
harryApplication.printData()
