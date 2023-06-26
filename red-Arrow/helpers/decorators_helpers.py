
def validata_input(method):
    def wrap(self):
        res = method(self)
        if not callable(self.validator):
            return res

        if callable(self.validator) and self.validator(res):
            return self.validator(res)
        return res if self.validator(res) else ''

    return wrap
