import os
from os.path import dirname, abspath, join

from nanohttp import Controller, context, Static, settings

from .templating import template


here = abspath(dirname(__file__))


class Root(Controller):
    static = Static(join(here, 'static'))

    @template('index.mak')
    def index(self, *args):
        root = settings.root
        return dict(
            settings=settings,
            environ=context.environ
        )

