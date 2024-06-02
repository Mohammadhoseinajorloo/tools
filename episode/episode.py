import urllib.request
import json 

def get_url_data(url):
    with urllib.request.urlopen(url) as req:
        info = req.read()

    loaded_info = json.loads(info)
    return loaded_info

def main():
    name = "mrrobot"
    url = f"https://www.episodate.com/api/search?q={name}"

    info = get_url_data(url)
    print(info)


if __name__ == "__main__":
    main()
