from fake_useragent import UserAgent

ua = UserAgent()
chosen_agent = ua.random

for i in range(100):
    print(ua.random)
