import socket
import ssl
from .MTalkException import MTalkException


class MTalkClient:
    def __init__(self, auth_data, proto_helper):
        self._auth_data = auth_data
        self._proto_helper = proto_helper

    def send_request(self):
        SUCCESS_RESPONSE_CODE = 3

        context = ssl.create_default_context()

        hostname = "mtalk.google.com"

        sock = socket.create_connection((hostname, 5228))
        try:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                ssock.write(self._proto_helper.get_mtalk_request(self._auth_data))
                ssock.read(1)
                resp_code = int(ssock.read(1)[0])
                if resp_code != SUCCESS_RESPONSE_CODE:
                    raise MTalkException(MTalkException.WRONG_RESPONSE, resp_code)
        except:
            pass
        finally:
            sock.close()
