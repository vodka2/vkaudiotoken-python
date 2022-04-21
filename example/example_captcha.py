from __future__ import print_function

try:
    import vkaudiotoken
except ImportError:
    import path_hack

from vkaudiotoken import get_kate_token, get_vk_official_token, TokenException
import sys

login = sys.argv[1]
password = sys.argv[2]
# for 2 factor authentication with sms
auth_code = sys.argv[3] if len(sys.argv) > 3 else 'GET_CODE'

captcha_sid = None
captcha_key = None
while True:
    try:
        print(get_kate_token(login, password, auth_code, captcha_sid, captcha_key))
        break
    except TokenException as err:
        if err.code == TokenException.CAPTCHA_REQ and 'captcha_sid' in err.extra:
            captcha_sid = err.extra['captcha_sid']
            captcha_key = input("Enter captcha key from image (" + err.extra["captcha_img"] + "): ")
        else:
            raise
