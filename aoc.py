#!/usr/bin/env python3

import pathlib
import os

CACHE_FOLDER = "input_cache"
CACHE_FILENAME = "input-{year}-{day:02d}.txt"

def read_input(year, day):
    # create cache pah if it doesn't exist
    path = os.path.dirname(__file__)
    path = os.path.join(path, CACHE_FOLDER)
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)  

    # check if file exists
    filename = os.path.join(path, CACHE_FILENAME.format(year=year, day=day))
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


def read_remote(year, day):
    import requests
    import yaml
    
    with open("cookies.yaml", "rt") as f:
        cookies = yaml.load(f, yaml.FullLoader)
    r = requests.get(
            "https://adventofcode.com/{}/day/{}/input".format(year, day), 
            cookies=cookies
        )
    
    return r.text

def file_from_template(args):
    if not os.path.isfile(args.file):
        with open(args.template, 'rt') as f:
            template = f.read()

        content = template.format(year=args.year, day=args.day)

        with open(args.file, 'wt') as f:
            f.write(content)
    else:
        print("File {} already exists. Doing nothing.".format(args.file))
    
if __name__ == "__main__":
    
    import argparse
    import datetime

    path = os.path.dirname(__file__)
    template = os.path.join(path, 'template.py')
    now = datetime.datetime.now()
    filename = os.path.join(path, "{year}-{day:02d}.py".format(year=now.year, day=now.day))

    parser = argparse.ArgumentParser(description="Creates a python file for an advent of code day from a template.")
        
    parser.add_argument(
        "-t", 
        "--template",
        help="Location of the template file to use. Defaults to {}".format(template), 
        default=template)

    parser.add_argument(
        "-f", 
        "--file",
        help="Location of the file to create. Defaults to year-day.py ({})".format(filename), 
        default=filename)

    parser.add_argument(
        "-y", 
        "--year", 
        type=int, 
        help="The year for which to initalize the template. Defaults to current year ({})".format(now.year), 
        default=now.year)

    parser.add_argument(
        "-d", 
        "--day", 
        type=int, 
        help="The day for which to initalize the template. Defaults to current day ({:02d})".format(now.day), 
        default=now.day)

    args = parser.parse_args()

    file_from_template(args)