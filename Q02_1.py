#######################
class RoseDictionary(dict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            raise KeyError("KeyError: 'error_msg'")

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def pop_item(self, raise_error=True, default=None, error_msg=''):
        if len(self) == 0:
            if raise_error:
                if error_msg:
                    raise KeyError(f"KeyError: '{error_msg}'")
                else:
                    raise KeyError("KeyError: 'error_msg'")
            else:
                return default
        else:
            key = next(reversed(self))
            value = self[key]
            del self[key]
            return (key, value)

    def get_item(self, key, raise_error=True, default=None, error_msg=''):
        try:
            return self[key]
        except KeyError:
            if raise_error:
                if error_msg:
                    raise KeyError(f"KeyError: '{error_msg}'")
                else:
                    raise KeyError("KeyError: 'error_msg'")
            else:
                return default
##################