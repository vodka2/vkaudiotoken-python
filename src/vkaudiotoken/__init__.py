from .AndroidCheckin import AndroidCheckin
from .CommonParams import CommonParams
from .MTalkClient import MTalkClient
from .MTalkException import MTalkException
from .ProtobufException import ProtobufException
from .SmallProtobufHelper import SmallProtobufHelper
from .TokenException import TokenException
from .TokenReceiver import TokenReceiver
from .TokenReceiverOfficial import TokenReceiverOfficial
from .TwoFAHelper import TwoFAHelper
from .VkClient import VkClient
from . import supported_clients


def get_kate_token(login, password, auth_code='GET_CODE', non_refreshed_token=None):
    params = CommonParams(supported_clients.KATE.user_agent)
    protobuf_helper = SmallProtobufHelper()

    checkin = AndroidCheckin(params, protobuf_helper)
    auth_data = checkin.do_checkin()

    mtalkClient = MTalkClient(auth_data, protobuf_helper)
    mtalkClient.send_request()

    receiver = TokenReceiver(login, password, auth_data, params, auth_code)
    return {'token': receiver.get_token(non_refreshed_token), 'user_agent': supported_clients.KATE.user_agent}


def get_vk_official_token(login, password, auth_code='GET_CODE'):
    params = CommonParams(supported_clients.VK_OFFICIAL.user_agent)
    receiver = TokenReceiverOfficial(login, password, params, auth_code)

    return {
        'token': receiver.get_token()['access_token'],
        'user_agent': supported_clients.VK_OFFICIAL.user_agent
    }
