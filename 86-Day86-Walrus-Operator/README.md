# Day 86: Walrus Operator in Python (`:=`) 🦭

## 📌 Overview
Welcome to **Day 86** of the 100 Days of Code challenge! Today, we explored the **Walrus Operator (`:=`)**, officially known as **Assignment Expressions** (introduced in Python 3.8). The walrus operator allows you to assign a value to a variable as part of a larger expression, reducing code redundancy and keeping loops or conditional checks concise.

---

## 💻 Key Concepts Covered Today

### 1. What is the Walrus Operator?
*   Represented by `:=` (resembling the eyes and tusks of a walrus).
*   Allows variable assignment **inside** expressions (such as `if` statements, `while` loops, or list comprehensions).

### 2. Primary Use Cases
*   **Loop Conditions:** Streamlining user input collection loops until a termination keyword (like `"quit"`) is entered.
*   **Avoiding Repeated Calculations:** Assigning evaluated values during conditional checks to avoid recalculating heavy functions or `len()` expressions multiple times.

---

## 🛠️ Code Snippet Example

```python
# --- 1. Basic Assignment in Conditional ---
if (a := len("Hello World")) > 5:
    print(f"String length is {a}, which is greater than 5")


# --- 2. Input Collection Loop with Walrus Operator ---
foods = list()
while (food := input("What food do you like? (type 'quit' to exit): ")) != "quit":
    foods.append(food)

print(f"Your favorite foods: {foods}")
