#!/usr/bin/python2
# coding: utf-8
# upload image to imgbb.com, get direct link.
import requests
import json
import sys

api_key = "" # api.imgbb.com to get one of these.
debug = False

def abort(error):
    if debug == True:
        print "\nBegin Error\n"
        print e
        print "\nEnd Error\n"
    sys.exit("Exception - Quitting!")

def upload_image(image, api_key):
    try:
        url = "https://api.imgbb.com/1/upload"
        data = {"key": api_key}
        files = {"image": open(image,"rb")}
        r = requests.post(url=url, data=data, files=files)
    except Exception, e:
        abort(error=e)
    try:
        parse = json.loads(r.text)
        print parse["data"]["display_url"]
    except Exception, e:
        abort(error=e)

def main(args):
    if len(args) != 2:
        sys.exit("use: %s /path/to/file.png" %(args[0]))
    upload_image(image=args[1], api_key=api_key)

if __name__ == "__main__":
    main(args=sys.argv)
