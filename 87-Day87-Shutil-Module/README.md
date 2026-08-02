# Day 87: Shutil Module in Python 📁📦

## 📌 Overview
Welcome to **Day 87** of the 100 Days of Code challenge! Today, we explored the **`shutil` (Shell Utilities) module** in Python. While the `os` module provides low-level operating system functions, `shutil` provides high-level operations for copying, moving, archiving, and deleting files and entire directory trees.

---

## 💻 Key Concepts Covered Today

### 1. Key Functions in `shutil` Module
*   **`shutil.copy(src, dst)`**: Copies the file at `src` to the location `dst`. Preserves file permissions but **not** metadata (creation/modification time).
*   **`shutil.copy2(src, dst)`**: Identical to `copy()`, but preserves file metadata (timestamps).
*   **`shutil.copytree(src, dst)`**: Recursively copies an entire directory tree from `src` to `dst`.
*   **`shutil.move(src, dst)`**: Recursively moves a file or directory to another location (acts as a rename operation if destination is in the same path).
*   **`shutil.rmtree(path)`**: Deletes an entire directory tree (removes directory and all its sub-contents). *Use with caution!*

---

## 🛠️ Code Snippet Example

```python
import shutil
import os

# 1. Copying a single file while preserving metadata
shutil.copy2("main.py", "main_backup.py")
print("File backed up successfully!")

# 2. Copying an entire directory tree recursively
# shutil.copytree("my_folder", "my_folder_backup")

# 3. Moving a file or directory
# shutil.move("main_backup.py", "backup_folder/main_backup.py")

# 4. Removing a directory and all of its contents recursively
# shutil.rmtree("backup_folder")
