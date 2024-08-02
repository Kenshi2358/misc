"""
Script to ssh onto servers faster.
"""
import os
from colorama import Fore, Style

server_container = {
    'v': 'vulture',
    'gg': 'greengoblin',
    't': 'thanos',
    'u': 'ultron',

    'd': 'drax',
    'f': 'fury',
    'gr': 'groot',
    'ga': 'gamora',
    'i': 'ironman',

    'r': 'rocket',
    's': 'spiderman',
    'ws': 'wintersoldier',
    'w': 'wolverine',
    'm': 'magneto',

    've': 'venom',
    'sh': 'shangchi',

    'a': 'abomination',
    'k': 'kang',
    'b': 'blade',

    'pj': 'prd-jenkins'
}

server_str1 = f"""
    provider dev:{Fore.CYAN}
    v - vulture, gg - greengoblin
    t - thanos, u - ultron{Style.RESET_ALL}

    provider prod:{Fore.GREEN}
    d - drax, f - fury
    gr - groot, ga - gamora
    i - ironman, r - rocket
    s - spiderman, ws - wintersoldier
    w - wolverine, m - magneto{Style.RESET_ALL}

    member dev:{Fore.YELLOW}
    ve - venom{Style.RESET_ALL}

    member prod:{Fore.MAGENTA}
    sh - shangchi{Style.RESET_ALL}

    misc:{Fore.LIGHTRED_EX}
    a - abomination, k - kang
    b - blade
    pj - prod jenkins{Style.RESET_ALL}
    """

user_answer1 = input(f'Choose from the server_container:\n{server_str1}\n')

for key, value in server_container.items():
    if user_answer1 == key:

        server_str1 = f'ssh {value}.des.mdx.med'

        print(f'Connecting to: {value}')
        os.system(server_str1)
        break

else:
    print('Answer not in server_container. Ending program.')
