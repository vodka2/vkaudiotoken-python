from __future__ import print_function

try:
    import vkaudiotoken
except ImportError:
    import path_hack

from vkaudiotoken import supported_clients
import sys
import requests
import json
import re

token = sys.argv[1]
user_agent = supported_clients.VK_OFFICIAL.user_agent

sess = requests.session()
sess.headers.update({'User-Agent': user_agent})


def get_mp3_from_m3u8(url):
    if 'index.m3u8?' not in url:
        return url
    if '/audios/' in url:
        return re.sub(r'^(.+?)/[^/]+?/audios/([^/]+)/.+$', '\\1/audios/\\2.mp3', url)
    else:
        return re.sub(r'^(.+?)/(p[0-9]+)/[^/]+?/([^/]+)/.+$', '\\1/\\2/\\3.mp3', url)


def prettyprint_mp3(result):
    print(re.sub(r'(?<=")https://.+?index.m3u8\?.+?(?=")', lambda m: get_mp3_from_m3u8(m.group(0)),
                 json.dumps(json.loads(result.content.decode('utf-8')), indent=2)))


prettyprint_mp3(sess.post(
    "https://api.vk.com/method/audio.getCatalog",
    data=[('access_token', token),
          ('https', 1),
          ('ref', 'search'),
          ('extended', 1),
          ('lang', 'en'),
          ('query', 'Justin Bieber - Baby'),
          ('v', '5.116')]
))
