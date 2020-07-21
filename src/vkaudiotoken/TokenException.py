class TokenException(Exception):
    REGISTRATION_ERROR = 0
    TOKEN_NOT_REFRESHED = 1
    TOKEN_NOT_RECEIVED = 2
    REQUEST_ERR = 3
    TWOFA_REQ = 4
    TWOFA_ERR = 5

    @property
    def extra(self):
        return self._extra

    @property
    def code(self):
        return self._code

    def __init__(self, code, extra=None):
        self._code = code
        self._extra = extra
        if extra is not None:
            extrastr = str(extra)
        else:
            extrastr = ''
        if code == TokenException.REGISTRATION_ERROR:
            super(TokenException, self).__init__("Registration error. Code: {0}".format(code))
        elif code == TokenException.TOKEN_NOT_REFRESHED:
            super(TokenException, self).__init__("Token was not refreshed, tokens are the same. Code: {0}".format(code))
        elif code == TokenException.TOKEN_NOT_RECEIVED:
            super(TokenException, self).__init__(
                "Can't obtain token. Code: {0}. Error extra: {1}".format(code, extrastr))
        elif code == TokenException.REQUEST_ERR:
            super(TokenException, self).__init__(
                "Error when making request. Code: {0}. Error extra: {1}".format(code, extrastr))
        elif code == TokenException.TWOFA_REQ:
            super(TokenException, self).__init__(
                "Two factor auth is required. Code: {0}. Error extra: {1}".format(code, extrastr))
        elif code == TokenException.TWOFA_ERR:
            super(TokenException, self).__init__(
                "2FA Error. Code: {0}. Error extra: {1}".format(code, extrastr))
