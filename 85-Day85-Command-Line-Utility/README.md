# Day 85: Command Line Utility in Python 💻

## 📌 Overview
Welcome to **Day 85** of the 100 Days of Code challenge! Today, we built a **Command Line Utility** in Python. Command Line Interface (CLI) utilities allow programs to be executed directly from the terminal or prompt, accepting flags, positional arguments, and options (using modules like `argparse` or `sys.argv`).

---

## 💻 Key Concepts Covered Today

### 1. What is a Command Line Utility?
*   A tool or script designed to run from the command line/terminal.
*   Enables automated batch tasks, server administration scripts, and quick utility operations without requiring a Graphical User Interface (GUI).

### 2. Core Modules Used
*   **`argparse`**: Python's standard library module for parsing command-line options and arguments cleanly with auto-generated help menus.
*   **`requests`**: Used to fetch or download data/files from remote URLs directly via CLI parameters.

---

## 🛠️ Code Snippet Example

```python
import argparse
import requests

def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    
    print(f"Downloading from {url} ...")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"File saved successfully as: {local_filename}")

parser = argparse.ArgumentParser(description="Command Line Utility to download files")

# Adding command line arguments
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", help="Name of the output file", default=None)

args = parser.parse_args()

# Execute utility
download_file(args.url, args.output)
