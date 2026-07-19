# Day 59: Decorators in Python 🎨

## 📌 Overview
Welcome to **Day 59** of the 100 Days of Code challenge! Today, we explored **Decorators** in Python. Decorators are a powerful and elegant tool that allows us to modify or extend the behavior of a function or method without permanently altering its actual source code. They are widely used in frameworks like Django and Flask for logging, authentication, and caching.

---

## 💻 Key Concepts Covered Today

### 1. What is a Decorator?
*   A decorator is a function that takes another function as an argument, adds some functionality or wrappers to it, and returns the modified function.
*   It uses the `@decorator_name` syntax placed right above the function definition.

### 2. Functions as First-Class Citizens
*   To understand decorators, we reviewed that in Python, functions can be passed as arguments to other functions, assigned to variables, and returned from other functions.

---

## 🛠️ Code Snippet Example

```python
# Defining a decorator function
def greet_decorator(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")
        fx(*args, **kwargs)
        print("Thanks for using this function.")
    return mfx

# Applying the decorator using @ syntax
@greet_decorator
def add(a, b):
    print(f"The sum is: {a + b}")

# Calling the decorated function
add(5, 7)
