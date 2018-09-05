import os
from os.path import dirname, abspath, join, isdir

from nanohttp import Controller, context, Static, settings, HTTPNotFound, \
    HTTPForbidden

from .templating import template


here = abspath(dirname(__file__))


class Node:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.isdirectory = isdir(join(settings.root, parent, name))

    @property
    def path(self):
        return join(self.parent, self.name)


class Root(Controller):
    static = Static(join(here, 'static'))

    @template('index.mak')
    def index(self, *args):
        root = settings.root
        virtual_path = '/' + '/'.join(args)
        physical_path = join(root, virtual_path)

        if '..' in virtual_path:
            raise HTTPForbidden()

        try:
            nodes = sorted(
                (Node(virtual_path, i) for i in os.listdir(physical_path)),
                key=lambda n: (not n.isdirectory, n.name)
            )
        except FileNotFoundError:
            raise HTTPNotFound()

        except PermissionError:
            raise HTTPForbidden()

        return dict(
            nodes=nodes,
            virtual_path=virtual_path
        )

