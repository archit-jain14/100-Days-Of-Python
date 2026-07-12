# Day 52: Lambda Functions in Python 🐍

## 📌 Overview
Welcome to **Day 52** of the 100 Days of Code challenge! Today, we explored **Lambda Functions** (also known as anonymous functions) in Python. These are short, single-expression functions that don't require a formal definition using the `def` keyword, making the code cleaner and more efficient for quick logic implementations.

---

## 💻 Key Concepts Covered Today

### 1. What is a Lambda Function?
*   An anonymous function defined using the `lambda` keyword.
*   Syntax: `lambda arguments: expression`
*   It can take any number of arguments but can only have **one single expression** which is evaluated and returned automatically.

### 2. Why use Lambda Functions?
*   **Conciseness:** Ideal for one-liner operations where defining a full function with `def` would be overkill.
*   **Functional Programming:** Heavily used as arguments to higher-order functions like `map()`, `filter()`, and `sorted()`.

---

## 🛠️ Code Snippet Example

```python
# Regular function vs Lambda function

# Using def keyword
def double(x):
    return x * 2

# Using lambda keyword
double_lambda = lambda x: x * 2

print(double(5))         # Outputs: 10
print(double_lambda(5))  # Outputs: 10

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(4, 5))    # Outputs: 20
