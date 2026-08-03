# Day 95: Regular Expressions in Python 🔍🔍

## 📌 Overview
Welcome to **Day 95** of the 100 Days of Code challenge! Today, we explored **Regular Expressions (RegEx)** in Python using the built-in **`re` module**. Regular expressions provide a powerful, flexible, and efficient way to search, match, extract, and manipulate string patterns (such as email addresses, phone numbers, URLs, or specific text structures).

---

## 💻 Key Concepts Covered Today

### 1. What are Regular Expressions?
*   A sequence of characters that forms a search pattern.
*   Used for pattern matching, data validation, and text parsing.

### 2. Common Functions in `re` Module
*   **`re.search(pattern, string)`**: Searches for the first occurrence of a pattern in a string.
*   **`re.findall(pattern, string)`**: Returns a list of all non-overlapping matches.
*   **`re.match(pattern, string)`**: Checks if the pattern matches at the beginning of the string.
*   **`re.sub(pattern, repl, string)`**: Replaces occurrences of the pattern with a replacement string.
*   **`re.compile(pattern)`**: Compiles a regex pattern for reuse and better performance.

### 3. Common RegEx Meta-characters
*   `[]` - A set of characters (e.g., `[a-z]`)
*   `\d` - Digits (0-9)
*   `\w` - Word characters (a-z, A-Z, 0-9, _)
*   `+` - One or more occurrences
*   `*` - Zero or more occurrences
*   `^` / `$` - Starts with / Ends with

---

## 🛠️ Code Snippet Example

```python
import re

text = """
Hello! Contact us at support@example.com or sales@company.org.
Order ID: #10293, Amount: $250.
"""

# 1. Extracting Email Addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print(f"Extracted Emails: {emails}")

# 2. Extracting Numbers
number_pattern = r'\d+'
numbers = re.findall(number_pattern, text)
print(f"Extracted Digits: {numbers}")

# 3. Replacing Text
masked_text = re.sub(email_pattern, "[REDACTED]", text)
print("\nMasked Text:")
print(masked_text.strip())
