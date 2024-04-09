import webbrowser

u1 = 'https://duckduckgo.com/'
u2 = 'https://duckduckgo.com/'
u3 = 'https://duckduckgo.com/'

u4 = 'https://duckduckgo.com/'
u5 = 'https://duckduckgo.com/'
u6 = 'https://duckduckgo.com/'

u7 = 'https://duckduckgo.com/'
u8 = 'https://duckduckgo.com/'
u9 = 'https://chat.openai.com'

url_list = []

for i in range(1, 10, 1):
    url_list.append(globals()[f'u{i}'])

# MacOS path.
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

for each_url in url_list:
    webbrowser.get(chrome_path).open(each_url)
