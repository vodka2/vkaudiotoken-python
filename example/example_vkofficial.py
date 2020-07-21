from __future__ import print_function

try:
    import vkaudiotoken
except ImportError:
    import path_hack

from vkaudiotoken import CommonParams, TokenReceiverOfficial, supported_clients
import sys

login = sys.argv[1]
password = sys.argv[2]
# for 2 factor authentication with sms, or pass GET_CODE to get code
auth_code = sys.argv[3] if len(sys.argv) > 3 else None

params = CommonParams(supported_clients.VK_OFFICIAL.user_agent)
receiver = TokenReceiverOfficial(login, password, params, auth_code)

print(receiver.get_token()['access_token'])
