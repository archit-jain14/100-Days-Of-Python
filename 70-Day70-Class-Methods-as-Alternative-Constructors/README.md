# Day 70: Class Methods as Alternative Constructors in Python 🛠️

## 📌 Overview
Welcome to **Day 70** of the 100 Days of Code challenge! Today, we explored how **Class Methods** can be used as **Alternative Constructors** in Python Object-Oriented Programming. In Python, a class can only have one `__init__` constructor. However, when we need to instantiate objects using data in different formats (such as parsing strings, comma-separated values, or JSON-like objects), class methods (`@classmethod`) provide an elegant way to act as additional constructors.

---

## 💻 Key Concepts Covered Today

### 1. Why Alternative Constructors?
*   Standard `__init__` methods expect parameters in a clean, specific format.
*   In real-world applications, raw data often arrives as unparsed strings (e.g., `"John-10000"`).
*   Class methods allow us to clean/parse raw data and return a newly instantiated object (`cls(...)`) directly, keeping our code clean and modular.

### 2. Common Naming Conventions
*   Alternative constructor class methods often start with `from_` (e.g., `from_string`, `from_dict`, `from_json`).

---

## 🛠️ Code Snippet Example

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = int(salary)

    # Class method acting as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split("-")
        return cls(name, salary)  # Instantiates and returns a new object

# Standard Instantiation
e1 = Employee("Archit", 90000)
print(f"Standard: {e1.name}, Salary: {e1.salary}")

# Instantiation using Alternative Constructor (Parsing hyphen-separated string)
string_data = "Rohan-80000"
e2 = Employee.from_string(string_data)
print(f"Alternative: {e2.name}, Salary: {e2.salary}")
