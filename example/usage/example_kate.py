from __future__ import print_function

try:
    import vkaudiotoken
except ImportError:
    import path_hack

from vkaudiotoken import supported_clients
import sys
import requests
import json

token = sys.argv[1]
user_agent = supported_clients.KATE.user_agent

sess = requests.session()
sess.headers.update({'User-Agent': user_agent})


def prettyprint(result):
    print(json.dumps(json.loads(result.content.decode('utf-8')), indent=2))


prettyprint(sess.get(
    "https://api.vk.com/method/audio.getById",
    params=[('access_token', token),
            ('audios', '371745461_456289486,-41489995_202246189'),
            ('v', '5.95')]
))
