import requests
from .TokenException import TokenException


class TwoFAHelper:
    def __init__(self, params):
        self._params = params

    def validate_phone(self, validation_sid):
        session = requests.session()
        self._params.set_common_vk(session)
        dec = session.get("https://api.vk.com/method/auth.validatePhone", params=[
            ('sid', validation_sid),
            ('v', '5.95')
        ]).json()
        if 'error' in dec or 'response' not in dec or dec['response'] != 1:
            raise TokenException(TokenException.TWOFA_ERR, dec)
