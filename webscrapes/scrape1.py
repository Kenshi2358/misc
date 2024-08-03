
import requests
from bs4 import BeautifulSoup

import time
import random

from fake_useragent import UserAgent
ua = UserAgent(browsers='chrome', platforms='pc')

current_user_agent = ua.random
print(f"user_agent: {current_user_agent}")

headers = {
    "User-Agent": current_user_agent,
    "cookie": "cE4rRkttd1JVVXZsT0lJTFdoM1UyOFZpU0lzM0ZLcVBHeDNFWXVDZE93WDNpQkFrTWdIMHBQV3EwLzRsWmxiRzZZSkVHZDRXaUVLaVl1V3IxQzVOOFNJRmR4YXJ5aUp2QlRKVGtnUDk0SlZ1em5jdG5mWWdUbEdyNkcyaFFMY0grTFVWNldLb2pZcFpWL1lMTWFYVGpBPT0tLU1oQythWjFGS0hoclRrQW5IbGFhT0E9PQ%3D%3D--33de8f78009db9249d0a2348810f065a4c697d71"
}

url_1 = "https://filmfreeway.com/festivals/"
# url_1 = "https://filmfreeway.com/robots.txt"

# with requests.Session() as s:
#     s.headers.update(headers)

results = requests.get(url_1, headers=headers)

print(f"status code: {results.status_code}")
#time.sleep(20)

pass


