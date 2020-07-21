import zlib
import requests


class AndroidCheckin:
    def __init__(self, params, proto_helper, str24=None):
        self._params = params
        self._proto_helper = proto_helper
        self._str24 = str24

    def do_checkin(self):
        session = requests.Session()
        self._params.set_common_gcm(session)
        compressobj = zlib.compressobj(6, zlib.DEFLATED, zlib.MAX_WBITS | 16)
        data = compressobj.compress(self._proto_helper.get_query_message(self._str24)) + compressobj.flush()
        session.headers.update({
            'Content-Type': 'application/x-protobuffer',
            'Content-Encoding': 'gzip',
            'Content-Length': str(len(data))
        })
        result = session.post("https://android.clients.google.com/checkin", data=data).content
        return self._proto_helper.decode_resp_message(result, self._str24 is None)

