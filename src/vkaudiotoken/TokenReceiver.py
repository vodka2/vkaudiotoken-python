from .supported_clients import KATE
from .TokenException import TokenException
import requests


class TokenReceiver:
    def __init__(self, login, password, auth_data, params, auth_code=None, scope='audio,offline'):
        self._params = params
        self._login = login
        self._password = password
        self._auth_code = auth_code
        self._auth_data = auth_data
        self._scope = scope
        self._client = KATE

    def get_token(self, non_refreshed_token=None):
        receipt = self._get_receipt()
        token = self._get_non_refreshed() if non_refreshed_token is None else non_refreshed_token
        return self._refresh_token(token, receipt)

    def _get_receipt(self):
        session = requests.Session()
        self._params.set_common_gcm(session)
        session.headers.update({
            'Authorization': 'AidLogin ' + self._auth_data['id'] + ':' + self._auth_data['token']
        })
        data = {
            "X-scope": "GCM",
            "X-osv": "23",
            "X-subtype": "54740537194",
            "X-app_ver": "460",
            "X-kid": "|ID|1|",
            "X-appid": self._params.generate_random_string(
                11,
                '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-'),
            "X-gmsv": "200313005",
            "X-cliv": "iid-12211000",
            "X-app_ver_name": "56 lite",
            "X-X-kid": "|ID|1|",
            "X-subscription": "54740537194",
            "X-X-subscription": "54740537194",
            "X-X-subtype": "54740537194",
            "app": "com.perm.kate_new_6",
            "sender": "54740537194",
            "device": self._auth_data['id'],
            "cert": "966882ba564c2619d55d0a9afd4327a38c327456",
            "app_ver": "460",
            "info": "U_ojcf1ahbQaUO6eTSP7b7WomakK_hY",
            "gcm_ver": "200313005",
            "plat": "0",
            "target_ver": "28"
        }
        result = session.post('https://android.clients.google.com/c2dm/register3', data=data).content.decode('ascii')
        receipt = result.split('|ID|1|:')[1]
        if receipt == 'PHONE_REGISTRATION_ERROR':
            raise TokenException(TokenException.REGISTRATION_ERROR, result)
        return receipt

    def _get_non_refreshed(self):
        session = requests.Session()
        self._params.set_common_vk(session)
        dec = session.get('https://oauth.vk.com/token',
                          params=[
                                     ('grant_type', 'password'),
                                     ('client_id', self._client.client_id),
                                     ('client_secret', self._client.client_secret),
                                     ('username', self._login),
                                     ('password', self._password),
                                     ('v', '5.95'),
                                     ('lang', 'en'),
                                     ('scope', self._scope)
                                 ] + self._params.get_two_factor_part(self._auth_code)).json()
        if 'error' in dec and dec['error'] == 'need_validation':
            raise TokenException(TokenException.TWOFA_REQ, dec)
        if 'user_id' not in dec:
            raise TokenException(TokenException.TOKEN_NOT_RECEIVED, dec)
        return dec['access_token']

    def _refresh_token(self, token, receipt):
        session = requests.Session()
        self._params.set_common_vk(session)
        dec = session.get('https://api.vk.com/method/auth.refreshToken',
                          params=[
                              ('access_token', token),
                              ('receipt', receipt),
                              ('v', '5.95')
                          ]).json()
        new_token = dec['response']['token']
        if new_token == token:
            raise TokenException(TokenException.TOKEN_NOT_REFRESHED)

        return new_token
