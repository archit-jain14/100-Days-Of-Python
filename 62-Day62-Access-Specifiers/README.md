# Day 62: Access Specifiers in Python 🔐

## 📌 Overview
Welcome to **Day 62** of the 100 Days of Code challenge! Today, we explored **Access Specifiers** (also known as Access Modifiers) in Python OOPs. Access specifiers are used to restrict access to class variables and methods from outside the class, aiding in encapsulation and data protection.

---

## 💻 Key Concepts Covered Today

### 1. Types of Access Specifiers
*   **Public Access Modifier (Default):** All variables and methods defined in a class are public by default. They can be accessed from anywhere (inside or outside the class).
*   **Private Access Modifier (`__` double underscore):** Variables/methods prefixed with `__` are intended to be private and cannot be accessed directly outside the class.
*   **Protected Access Modifier (`_` single underscore):** Variables/methods prefixed with `_` are intended to be protected (accessible within the class and its subclasses). Note: This is purely a convention in Python and not strictly enforced by the interpreter.

### 2. Name Mangling in Python
*   Python doesn't have true private variables. Instead, it uses **Name Mangling** for private attributes.
*   A private attribute `__name` inside class `Employee` gets transformed internally to `_Employee__name`.
*   This prevents accidental overrides in subclasses while still allowing indirect access if necessary: `obj._ClassName__private_attribute`.

---

## 🛠️ Code Snippet Example

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name           # Public attribute
        self.__salary = salary     # Private attribute (Name Mangled)

# Creating Object
emp = Employee("Archit", 85000)

# Accessing Public Attribute
print(emp.name)  # Outputs: Archit

# Direct access to private attribute will raise an AttributeError:
# print(emp.__salary) 

# Accessing Private Attribute via Name Mangling
print(emp._Employee__salary)  # Outputs: 85000
