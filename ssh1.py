"""
Script to ssh onto servers faster.
"""
import os

server_container = {
    'f': 'fury',
    'v': 'vulture',
    't': 'thanos',
    'k': 'kang',
    'a': 'abomination',
    'gg': 'greengoblin',
    'u': 'ultron',
    'd': 'drax',
    'ga': 'gamora',
    'r': 'rocket',
    'w': 'wolverine',
    'ws': 'wintersoldier',
    'm': 'magneto'
}

user_answer1 = input(f'Choose from the server_container:\n{server_container}\n')


for key, value in server_container.items():
    if user_answer1 == key:

        server_str1 = f'ssh {value}.des.mdx.med'
        print(f'Connecting to: {value}')
        os.system(server_str1)
        break

else:
    print('Answer not in server_container. Ending program.')
