import requests
from .supported_clients import VK_OFFICIAL
from .TokenException import TokenException


class TokenReceiverOfficial:
    def __init__(self, login, password, params, auth_code=None, scope='all'):
        self._login = login
        self._password = password
        self._params = params
        self._auth_code = auth_code
        self._scope = scope
        self._client = VK_OFFICIAL

    def get_token(self):
        return self._get_non_refreshed()

    def _get_non_refreshed(self):
        session = requests.Session()
        self._params.set_common_vk(session)
        device_id = self._params.generate_random_string(16, '0123456789abcdef')
        dec = session.get('https://oauth.vk.com/token',
                          params=[
                                     ('grant_type', 'password'),
                                     ('client_id', self._client.client_id),
                                     ('client_secret', self._client.client_secret),
                                     ('username', self._login),
                                     ('password', self._password),
                                     ('v', '5.116'),
                                     ('lang', 'en'),
                                     ('scope', self._scope),
                                     ('device_id', device_id)
                                 ] + self._params.get_two_factor_part(self._auth_code)).json()

        if 'error' in dec and dec['error'] == 'need_validation':
            raise TokenException(TokenException.TWOFA_REQ, dec)
        if 'user_id' not in dec:
            raise TokenException(TokenException.TOKEN_NOT_RECEIVED, dec)
        return {'access_token': dec['access_token']}
