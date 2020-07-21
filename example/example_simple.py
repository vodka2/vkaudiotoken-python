from __future__ import print_function

try:
    import vkaudiotoken
except ImportError:
    import path_hack

from vkaudiotoken import get_kate_token, get_vk_official_token
import sys

login = sys.argv[1]
password = sys.argv[2]
# for 2 factor authentication with sms
auth_code = sys.argv[3] if len(sys.argv) > 3 else 'GET_CODE'

print(get_kate_token(login, password, auth_code))
print(get_vk_official_token(login, password, auth_code))