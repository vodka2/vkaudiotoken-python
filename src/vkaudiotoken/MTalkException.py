class MTalkException(Exception):
    WRONG_RESPONSE = 1

    @property
    def extra(self):
        return self._extra

    @property
    def code(self):
        return self._code

    def __init__(self, code, extra=None):
        self._extra = extra
        self._code = code
        if code == MTalkException.WRONG_RESPONSE:
            super(MTalkException, self).__init__('Wrong response code {0}. Code: {1}'.format(extra, code))
