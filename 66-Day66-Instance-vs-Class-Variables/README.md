# Day 66: Instance vs Class Variables in Python 📊

## 📌 Overview
Welcome to **Day 66** of the 100 Days of Code challenge! Today, we explored the differences between **Instance Variables** and **Class Variables** in Python Object-Oriented Programming. Knowing when to use class-level storage versus object-level storage helps optimize memory usage and state management across your application.

---

## 💻 Key Concepts Covered Today

### 1. Class Variables
*   Variables that are defined directly inside the class body (outside any methods).
*   They are **shared among all instances** (objects) of that class.
*   Changing a class variable using the Class Name updates it for all objects (unless an instance has overridden it).

### 2. Instance Variables
*   Variables that are defined inside methods (usually inside `__init__`) using `self`.
*   They are **unique to each instance** of the class.
*   Modifying an instance variable on one object will not affect any other object.

---

## 🛠️ Code Snippet Example

```python
class Employee:
    # Class Variable (Shared across all employees)
    company_name = "Tech Corp"
    no_of_employees = 0

    def __init__(self, name, salary):
        self.name = name           # Instance Variable
        self.salary = salary       # Instance Variable
        Employee.no_of_employees += 1

    def show_details(self):
        print(f"Name: {self.name} | Salary: {self.salary} | Company: {self.company_name}")

# Creating Objects
emp1 = Employee("Archit", 80000)
emp2 = Employee("Rohan", 60000)

# Displaying Info
emp1.show_details()  # Uses class-level company_name
emp2.show_details()

# Overriding class variable for a specific instance
emp1.company_name = "Tech Corp India"
print(emp1.company_name)  # Outputs: Tech Corp India
print(emp2.company_name)  # Outputs: Tech Corp

print(f"Total Employees: {Employee.no_of_employees}")  # Outputs: 2
