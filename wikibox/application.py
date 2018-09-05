from nanohttp import Application

from .controllers import Root


class WikiBox(Application):
    def __init__(self):
        super().__init__(Root())

