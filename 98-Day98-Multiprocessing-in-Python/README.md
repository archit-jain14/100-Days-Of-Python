# Day 98: Multiprocessing in Python ⚙️🔥

## 📌 Overview
Welcome to **Day 98** of the 100 Days of Code challenge! Today, we explored **Multiprocessing** in Python using the built-in **`multiprocessing`** module and **`concurrent.futures.ProcessPoolExecutor`**. Unlike Multithreading, Multiprocessing spawns separate Python process instances (each with its own Python interpreter and memory space), bypassing Python's Global Interpreter Lock (GIL) and taking full advantage of multi-core CPUs.

---

## 💻 Key Concepts Covered Today

### 1. What is Multiprocessing?
*   Executes processes in parallel across multiple CPU cores.
*   **Multithreading vs. Multiprocessing:** Multithreading is best for I/O-bound tasks, while Multiprocessing excels at CPU-bound computation tasks (data processing, image/video processing, heavy calculations).

### 2. Core Modules & Methods
*   **`multiprocessing.Process(target, args)`**: Spawns a new independent process.
*   **`p.start()` & `p.join()`**: Starts execution and waits for process completion.
*   **`ProcessPoolExecutor`**: Manages a pool of worker processes to execute calls asynchronously.

---

## 🛠️ Code Snippet Example

```python
import multiprocessing
import requests

def downloadFile(url, name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    url = "[https://picsum.photos/200/300](https://picsum.photos/200/300)"
    processes = []

    # Spawning multiple processes
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        processes.append(p)

    # Ensuring all processes complete
    for p in processes:
        p.join()
