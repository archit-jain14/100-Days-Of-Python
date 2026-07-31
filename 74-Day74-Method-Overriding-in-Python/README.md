# Day 74: Method Overriding in Python 🔄

## 📌 Overview
Welcome to **Day 74** of the 100 Days of Code challenge! Today, we explored **Method Overriding** in Python Object-Oriented Programming. Method overriding is a concept related to polymorphism and inheritance that allows a child class to provide a specific implementation of a method that is already defined in its parent class.

---

## 💻 Key Concepts Covered Today

### 1. What is Method Overriding?
*   Redefining a method in a child class that shares the **same name** and **same parameter signature** as a method in its parent class.
*   When the overridden method is invoked on an instance of the child class, the child's implementation is executed instead of the parent's.

### 2. Retaining Parent Class Logic with `super()`
*   If you override a method but still want to execute the base implementation from the parent class, you can call `super().method_name()` inside the overridden method.

---

## 🛠️ Code Snippet Example

```python
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    # Method Overriding: Replacing Shape's area() implementation
    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Method Overriding: Specifying Circle's area formula
    def area(self):
        return 3.14 * self.radius * self.radius

# Creating Instances
rect = Rectangle(10, 5)
circ = Circle(7)

print(f"Rectangle Area: {rect.area()}")  # Output: 50
print(f"Circle Area: {circ.area()}")     # Output: 153.86
