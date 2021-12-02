from math import floor, ceil
import re
from pprint import pprint

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import yaml

with open("cookies.yaml", "rt") as f:
        cookies = yaml.load(f, yaml.FullLoader)


boards = [
        dict(name='pro', url="https://adventofcode.com/2020/leaderboard/private/view/198336"),
        dict(name='noob', url="https://adventofcode.com/2020/leaderboard/private/view/993406")
        ]

users = dict()

for board in boards:
    r = requests.get(
        board['url'], 
        cookies=cookies
    )

    RE_BOARD_ROW = r"^\s*(?P<place>\d+)\)\s+(?P<score>\d+)\s+\*+\s+(?P<name>.+)$"

    soup = BeautifulSoup(r.text, 'html.parser')
    users[board['name']] = [re.match(RE_BOARD_ROW, div.text).groupdict() for div in soup.find_all('div', {'class':'privboard-row'})[1:]]
    me, *_ = [user for user in users[board['name']] if user['name'] == '(anonymous user #1173836)']
    pprint("{} : {}".format(board['name'], me))

plot_width = ceil(len(boards)**0.5)
plot_height = floor(len(boards)**0.5)

fig, ax = plt.subplots(plot_width, plot_height)
ax = ax.ravel()

for n, board in enumerate(boards):
    ax[n].set_title(board['name'])
    mepos, *_ = [i for i, user in enumerate(users[board['name']]) if user['name'] == '(anonymous user #1173836)']
    colors = ['gray']*mepos + ['red'] + ['gray']*((len(users[board['name']]) - mepos)-1)
    # print(colors)
    # print(len(colors))
    # print(len(users[board['name']]))
    ax[n].bar(range(1, len(users[board['name']])+1), [int(user['score']) for user in users[board['name']]], color=colors)

plt.show()