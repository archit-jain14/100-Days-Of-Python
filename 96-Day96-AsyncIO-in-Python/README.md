# Day 96: AsyncIO in Python ⚡🔄

## 📌 Overview
Welcome to **Day 96** of the 100 Days of Code challenge! Today, we explored **AsyncIO** in Python using the built-in **`asyncio` module**. AsyncIO is a library used to write concurrent code using the `async`/`await` syntax. It is ideal for I/O-bound operations (such as downloading files, API requests, and database queries) where waiting for external resources shouldn't block the main thread.

---

## 💻 Key Concepts Covered Today

### 1. What is Asynchronous Programming?
*   Allows multiple tasks to run concurrently without waiting for each task to finish sequentially.
*   **`async def`**: Used to declare a coroutine function.
*   **`await`**: Pauses the execution of the coroutine until the awaited task completes, yielding control back to the event loop.

### 2. Core Functions in `asyncio`
*   **`asyncio.run(coroutine)`**: Entry point for running an async main function and managing the event loop.
*   **`asyncio.gather(*tasks)`**: Executes multiple coroutines concurrently and waits for all of them to complete.
*   **`asyncio.sleep(seconds)`**: Non-blocking delay function to simulate asynchronous I/O tasks.

---

## 🛠️ Code Snippet Example

```python
import asyncio

async def function1():
    print("Task 1 started...")
    await asyncio.sleep(2)
    print("Task 1 completed!")
    return "Result 1"

async def function2():
    print("Task 2 started...")
    await asyncio.sleep(1)
    print("Task 2 completed!")
    return "Result 2"

async def main():
    # Executing functions concurrently using asyncio.gather
    results = await asyncio.gather(
        function1(),
        function2()
    )
    print(f"All tasks completed. Results: {results}")

# Run event loop
asyncio.run(main())
