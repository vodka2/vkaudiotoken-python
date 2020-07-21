class ProtobufException(Exception):
    SYMBOL = 0
    NOT_FOUND = 1

    @property
    def sym(self):
        return self._sym

    @property
    def code(self):
        return self._code

    def __init__(self, code, sym=None):
        self._code = code
        self._sym = sym
        if code == ProtobufException.SYMBOL:
            super(ProtobufException, self).__init__('Unexpected symbol code: {0}. Code: {1}'.format(sym, code))
        elif code == ProtobufException.NOT_FOUND:
            super(ProtobufException, self).__init__('Id and token were not found. Code: {0}'.format(code))
