# Day 89: Requests Module & Web Scraping in Python 🌐🕷️

## 📌 Overview
Welcome to **Day 89** of the 100 Days of Code challenge! Today, we explored the **`requests` module** in Python along with basic **Web Scraping** using **BeautifulSoup**. The `requests` module is an elegant and simple HTTP library used to interact with web servers, consume REST APIs, and fetch raw web page HTML content for data extraction.

---

## 💻 Key Concepts Covered Today

### 1. HTTP Methods with `requests`
*   **`requests.get(url)`**: Sends an HTTP GET request to retrieve data or web pages from a specified URL.
*   **`requests.post(url, data/json)`**: Sends data to a server (e.g., submitting forms or posting payload to APIs).

### 2. Web Scraping with BeautifulSoup (`bs4`)
*   Parsing raw HTML content returned by `response.text`.
*   Using CSS selectors (`soup.find()`, `soup.find_all()`, `soup.select()`) to extract specific tags, headings, links, and text content from websites.

---

## 🛠️ Code Snippet Example

```python
import requests
from bs4 import BeautifulSoup

# 1. Fetching Web Page HTML
url = "[https://www.codewithharry.com](https://www.codewithharry.com)"
response = requests.get(url)

print(f"Status Code: {response.status_code}")

# 2. Parsing HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting page title and all headings
print(f"Page Title: {soup.title.string}")

for heading in soup.find_all("h2"):
    print(f"Heading: {heading.text.strip()}")
