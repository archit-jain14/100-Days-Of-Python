# Day 60: Getters and Setters in Python ⚙️

## 📌 Overview
Welcome to **Day 60** of the 100 Days of Code challenge! Today, we explored **Getters and Setters** in Python Object-Oriented Programming. In Python, these are implemented beautifully using the `@property` decorator. They allow us to treat class methods like attributes, providing a clean way to add data validation and encapsulation without breaking the external API of our classes.

---

## 💻 Key Concepts Covered Today

### 1. What is a Getter?
*   A method that allows you to access the value of an attribute, but treats it like a regular property.
*   It is defined using the `@property` decorator above the method.

### 2. What is a Setter?
*   A method that allows you to set or change the value of an attribute while enabling data validation or modification under the hood.
*   It is defined using the `@<getter_method_name>.setter` decorator.

---

## 🛠️ Code Snippet Example

```python
class MyValue:
    def __init__(self, value):
        self._value = value  # Internal naming convention for private variables

    # Getter method
    @property
    def ten_x_value(self):
        return 10 * self._value

    # Setter method
    @ten_x_value.setter
    def ten_x_value(self, new_value):
        self._value = new_value / 10

# Creating an object
obj = MyValue(10)

# Accessing the getter like an attribute (No parenthesis needed!)
print(obj.ten_x_value)  # Outputs: 100

# Using the setter to change the value dynamically
obj.ten_x_value = 67
print(obj._value)       # Outputs: 6.7
