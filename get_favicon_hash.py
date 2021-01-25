#!/usr/bin/python
import mmh3
import requests
import codecs
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_hash(url):
    url = url + "/favicon.ico"
    response = requests.get(url=url, verify=False)
    favicon = codecs.encode(response.content,"base64")
    hash = mmh3.hash(favicon)
    return hash

def main(args):
    if len(args) != 2:
        sys.exit("use: script.py https://lol.com")
    print get_hash(url=args[1])

if __name__ == "__main__":
    main(args=sys.argv)
