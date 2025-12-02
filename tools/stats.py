#!/usr/bin/env python3

from math import floor, ceil
import re
from pprint import pprint

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import yaml

def row_to_user(row):
    try:
        position = int(re.sub(r"\D", "", row.find('span', {'class': 'privboard-position'}).decode_contents()))
        score = int(re.sub(r"\D", "", row.find('span', {'class': 'privboard-position'}).find_next_sibling(string=True)))
        name = row.find('span', {'class': 'privboard-name'}).decode_contents().strip()

        return dict(
            position=position, 
            score=score,
            name=name
        )
    except Exception as e:
        return None
    
with open("cookies.yaml", "rt") as f:
        cookies = yaml.load(f, yaml.FullLoader)


boards = [
        dict(name='anon', url="https://adventofcode.com/2025/leaderboard/private/view/383378"),
        dict(name='namefags', url="https://adventofcode.com/2025/leaderboard/private/view/993406")
        ]

users = dict()

for board in boards:
    r = requests.get(
        board['url'], 
        cookies=cookies
    )

    soup = BeautifulSoup(r.text, 'html.parser')
    rows = [name.parent for name in soup.find_all('span', {'class':'privboard-name'})]
    users[board['name']] = list(filter(None, map(row_to_user, rows)))
    me, *_ = [user for user in users[board['name']] if user['name'] == '(anonymous user #1173836)']
    print(f"{'#'*10} {board['name']} {'#'*10}")
    pprint(me)

plot_width = ceil(len(boards)**0.5)
plot_height = floor(len(boards)**0.5)

fig, ax = plt.subplots(plot_width, plot_height)
ax = ax.ravel()

for n, board in enumerate(boards):
    ax[n].set_title(board['name'])
    mepos, *_ = [i for i, user in enumerate(users[board['name']]) if user['name'] == '(anonymous user #1173836)']
    colors = ['gray']*mepos + ['red'] + ['gray']*((len(users[board['name']]) - mepos)-1)
    ax[n].bar(range(1, len(users[board['name']])+1), [int(user['score']) for user in users[board['name']]], color=colors)

plt.show()