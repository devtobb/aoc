# boiler plate
def read_input(filename):
    import os
    import requests
    import yaml
    
    date, _ = os.path.splitext(os.path.basename(filename))
    year, day = date.split("-")
    
    with open("cookies.yaml", "rt") as f:
        cookies = yaml.load(f, yaml.FullLoader)
    r = requests.get(
            "https://adventofcode.com/{}/day/{}/input".format(year, day), 
            cookies=cookies
        )
    
    return r.text
