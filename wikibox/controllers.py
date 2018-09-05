import os
from os.path import dirname, abspath, join, isdir, split

from nanohttp import Controller, context, Static, settings, HTTPNotFound, \
    HTTPForbidden
import markdown2

from .templating import template


here = abspath(dirname(__file__))


class Node:
    def __init__(self, parent, name):
        self.parent = parent
        self.isdirectory = isdir(join(settings.root, parent, name))
        self.name = f'{name}{"/" if self.isdirectory else ""}'

    @property
    def path(self):
        return join(self.parent, self.name)


class Root(Controller):
    static = Static(join(here, 'static'))

    def get_nodes(self, virtual_path):
        physical_path = join(settings.root, virtual_path)

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

        nodes = [n for n in nodes if n.isdirectory or n.name.endswith('.md')]
        return nodes

    @template('index.mak')
    def index(self, *args):
        virtual_path = '/'.join(args)
        physical_path = join(settings.root, virtual_path)

        if not isdir(physical_path):
            virtual_path, filename = split(virtual_path)
        else:
            filename = ''

        if filename:
            html = markdown2.markdown_path(
                physical_path,
                extras=['tables', 'fenced-code-blocks']
            )
        else:
            html = ''

        parent_nodes = []
        if virtual_path:
            parents = virtual_path.split('/')
            for i, p in enumerate(parents):
                parent_nodes.append(Node('/'.join(parents[:i]), p))

        return dict(
            nodes=self.get_nodes(virtual_path),
            directory=virtual_path,
            filename=filename,
            parents=parent_nodes,
            content=html
        )

