# Day 69: Class Methods in Python 🛠️

## 📌 Overview
Welcome to **Day 69** of the 100 Days of Code challenge! Today, we explored **Class Methods** in Python Object-Oriented Programming. Class methods are bound to the class itself rather than individual instances. They allow us to access and modify class-level state directly, making them essential when dealing with factory methods or class attribute manipulation.

---

## 💻 Key Concepts Covered Today

### 1. What is a Class Method?
*   A method that receives the class itself (`cls`) as an implicit first parameter instead of an instance (`self`).
*   Defined using the `@classmethod` decorator.
*   Can access and modify class attributes that apply across all instances of the class.

### 2. Difference Between Instance, Class, and Static Methods
*   **Instance Method:** Takes `self` as the first argument; operates on specific object instances.
*   **Class Method:** Takes `cls` as the first argument; operates on the class itself (`@classmethod`).
*   **Static Method:** Takes no implicit first argument (`self` or `cls`); acts as an isolated utility function (`@staticmethod`).

---

## 🛠️ Code Snippet Example

```python
class Employee:
    company_name = "Tech Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name} | Salary: {self.salary} | Company: {self.company_name}")

    # Class Method to modify class variable
    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

# Creating Object
emp1 = Employee("Archit", 90000)
emp1.show_details()  # Company: Tech Corp

# Changing company name for ALL instances using the class method
Employee.change_company("Tech Corp Global")

emp1.show_details()  # Company: Tech Corp Global
