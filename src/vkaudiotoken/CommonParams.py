from .supported_clients import KATE
import random


class CommonParams:
    def __init__(self, vk_ua=None, gcm_ua=None):
        if vk_ua is None:
            self._vk_ua = KATE.user_agent
        else:
            self._vk_ua = vk_ua

        if gcm_ua is None:
            self._gcm_ua = 'Android-GCM/1.5 (generic_x86 KK)'
        else:
            self._gcm_ua = gcm_ua

    def get_two_factor_part(self, code=None):
        if code is None:
            return []
        return [
                   ('2fa_supported', 1),
                   ('force_sms', 1)
               ] + [] if code == 'GET_CODE' else [('code', code)]

    def generate_random_string(self, length, characters):
        return ''.join(random.choice(characters) for _ in range(length))

    def set_common_vk(self, session):
        session.headers.update({'User-Agent': self._vk_ua})

    def set_common_gcm(self, session):
        session.headers.update({'User-Agent': self._gcm_ua})
