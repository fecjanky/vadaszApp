def get_from_dict(dict, key, default):
    return dict[key] if key in dict else default


def add_to_class_repository(f):
    def wrapped(self,*args, **kwargs):
        f(self,*args, **kwargs)
        self.repository()[self.name()] = self

    return wrapped
