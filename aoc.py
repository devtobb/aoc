#!/usr/bin/env python3
import os
import stat

def file_from_template(args):
    if not os.path.isfile(args.file):
        with open(args.template, 'rt') as f:
            template = f.read()

        content = template.format(year=args.year, day=args.day)

        with open(args.file, 'wt') as f:
            f.write(content)
        
        # make executable by world
        st = os.stat(args.file)
        os.chmod(args.file, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH )

    else:
        print("File {} already exists. Doing nothing.".format(args.file))
    
if __name__ == "__main__":
    
    import argparse
    import datetime

    path = os.path.dirname(__file__)
    template = os.path.join(path, 'template.py')
    now = datetime.datetime.now()

    parser = argparse.ArgumentParser(description="Creates a python file for an advent of code day from a template.")
        
    parser.add_argument(
        "-t", 
        "--template",
        help="Location of the template file to use. Defaults to {}".format(template), 
        default=template)

    parser.add_argument(
        "-f", 
        "--file",
        help="Location of the file to create. Defaults to year-day.py")

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

    if not args.file:
        args.file =  os.path.join(path, str(args.year), "{year}-{day:02d}.py".format(year=args.year, day=args.day))


    file_from_template(args)