# boiler plate
def read_input(year, day):
    import requests
    import yaml
    
    with open("cookies.yaml", "rt") as f:
        cookies = yaml.load(f, yaml.FullLoader)
    r = requests.get(
            "https://adventofcode.com/{}/day/{}/input".format(year, day), 
            cookies=cookies
        )
    
    return r.text
