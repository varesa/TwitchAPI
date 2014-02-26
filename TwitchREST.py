import urllib.parse
import urllib.request

import json

baseUrl = "https://api.twitch.tv/kraken/"


def get(path):
    url = urllib.parse.urljoin(baseUrl, path)
    request = urllib.request.Request(url)
    request.add_header('Accept', "application/vnd.twitchtv.v3+json")
    raw_data = urllib.request.urlopen(request).read()
    return json.loads(raw_data.decode("utf-8"))


def post(path, data):
    url = urllib.parse.urljoin(baseUrl, path)
    return urllib.request.urlopen(url, data=data).read()
