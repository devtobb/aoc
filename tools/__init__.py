import os
import pathlib

CACHE_FOLDER = "input_cache"
CACHE_FILENAME = "input-{year}-{day:02d}{suffix}.txt"

class blist(list):
    def __rshift__(self, other):
        return blist(map(other, self))

def read_input(year: int, day: int, suffix: str = "") -> str:
    # create cache pah if it doesn't exist
    path = os.path.dirname(__file__)
    path = os.path.join(path, CACHE_FOLDER)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)  

    # check if file exists
    filename = os.path.join(path, CACHE_FILENAME.format(year=year, day=day, suffix=suffix))
    if os.path.isfile(filename):
        # read input from cache file
        with open(filename, 'rt') as f:
            content = f.read()
    else:
        # read input from remote, save to file then
        content = read_remote(year, day)
        with open(filename, 'wt') as f:
            f.write(content)

    return content


def read_remote(year: int, day: int) -> str:
    import requests
    import yaml
    
    cookie_file = os.path.join(os.path.dirname(__file__), "cookies.yaml")
    with open(cookie_file, "rt") as f:
        cookies = yaml.load(f, yaml.FullLoader)
    r = requests.get(
            "https://adventofcode.com/{}/day/{}/input".format(year, day), 
            cookies=cookies
        )
    return r.text
    