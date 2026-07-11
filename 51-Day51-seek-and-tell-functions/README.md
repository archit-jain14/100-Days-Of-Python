# Day 51: Seek and Tell Functions in Python 📂

## 📌 Overview
Welcome to **Day 51** of the 100 Days of Code challenge! Today's focus is on mastering advanced file handling operations in Python. While reading and writing files linearly is standard, today we explored how to precisely navigate and manipulate the file pointer using the built-in `seek()` and `tell()` functions, along with file truncation.

---

## 💻 Key Concepts Covered Today

### 1. The `tell()` Method
*   Used to find the **current position** of the file pointer (in bytes) within a file.
*   Helps track how much data has been read or where the next write operation will begin.

### 2. The `seek()` Method
*   Used to **move the file pointer** to a specific position within a file.
*   Syntax: `f.seek(offset)` where `offset` moves the pointer to that specific byte from the beginning of the file.

### 3. Truncating Files (`truncate()`)
*   Used to reduce or resize the file to a specified size (in bytes).
*   If you write data and want to cut off everything after a certain point, `truncate()` modifies the actual file size on the disk.

---

## 🛠️ Code Snippet Example

```python
with open("sample.txt", "w+") as f:
    f.write("Hello World!")
    
    # Check current position
    print(f.tell()) # Outputs: 12
    
    # Move pointer back to the beginning
    f.seek(0)
    print(f.read(5)) # Outputs: Hello
