from __future__ import print_function

try:
    import vkaudiotoken
except ImportError:
    import path_hack

from vkaudiotoken import CommonParams, SmallProtobufHelper, TokenReceiver, AndroidCheckin, MTalkClient, \
    supported_clients
import sys

params = CommonParams()
protobuf_helper = SmallProtobufHelper()

checkin = AndroidCheckin(params, protobuf_helper)
auth_data = checkin.do_checkin()

mtalkClient = MTalkClient(auth_data, protobuf_helper)
mtalkClient.send_request()

# This dict element is needed only for MTalk request
del auth_data['id_str']

# You can get multiple tokens using this data
print(auth_data)

login = sys.argv[1]
password = sys.argv[2]
# for 2 factor authentication with sms, or pass GET_CODE to get code
auth_code = sys.argv[3] if len(sys.argv) > 3 else None
receiver = TokenReceiver(login, password, auth_data, params, auth_code)
print(receiver.get_token())
