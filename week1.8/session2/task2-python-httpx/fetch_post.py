"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object
statusCode = response.status_code
print(statusCode)
if statusCode == 200:
    print(response.json())
     # response object, json() method
