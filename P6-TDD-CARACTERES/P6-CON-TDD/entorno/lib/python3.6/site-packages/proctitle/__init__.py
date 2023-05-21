import setproctitle

class ProcTitle:
    def __init__(self, title, replace=False):
        self.title = title
        self.replace = replace

    def __enter__(self):
        self.orig_title = setproctitle.getproctitle()
        if self.replace:
            setproctitle.setproctitle(self.title)
        else:
            setproctitle.setproctitle("{} - {}".format(
                self.orig_title,
                self.title,
            ))

    def __exit__(self, type, value, traceback):
        setproctitle.setproctitle(self.orig_title)

    def __call__(self, f):
        def wrapped(*args, **kwargs):
            with self:
                return f(*args, **kwargs)
        return wrapped

