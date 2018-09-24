import re
import os
from os.path import dirname, abspath, join, isdir, split

from nanohttp import Controller, context, Static, settings, HTTPNotFound, \
    HTTPForbidden
import markdown2

from .templating import template


here = abspath(dirname(__file__))


class Node:
    verb = None
    subject = None
    title = None

    def __init__(self, parent, name):
        self.parent = parent
        self.isdirectory = isdir(join(settings.root, parent, name))
        self.realname = name

        if not self.isdirectory and not self.hidden:
            name = re.sub('[-]+', ' ', name)[:-3]
            self.verb, self.subject, self.title = name.split(' ', 2)
        else:
            self.title = name

    @property
    def path(self):
        return join(self.parent, self.realname)

    @property
    def hidden(self):
        return re.search('[-]{2}.*\.md$', self.realname) is None


class Root(Controller):
    static = Static(join(here, 'static'))

    def get_nodes(self, virtual_path):
        physical_path = join(settings.root, virtual_path)

        if '..' in virtual_path:
            raise HTTPForbidden()

        try:
            nodes = sorted(
                (Node(virtual_path, i) for i in os.listdir(physical_path)),
                key=lambda n: (not n.isdirectory, n.title)
            )
        except FileNotFoundError:
            raise HTTPNotFound()

        except PermissionError:
            raise HTTPForbidden()

        nodes = [
            n for n in nodes if n.isdirectory or not n.hidden
        ]
        return nodes

    @template('index.mak')
    def index(self, *args):
        given_path = '/'.join(args)
        physical_path = join(settings.root, given_path)

        if not isdir(physical_path):
            if not given_path.endswith('.md'):
                raise HTTPForbidden(f'File Not allowed: {given_path}')

            virtual_path, filename = split(given_path)
        else:
            virtual_path = given_path
            filename = ''

        if filename:
            try:
                html = markdown2.markdown_path(
                    physical_path,
                    extras=[
                        'tables', 
                        'fenced-code-blocks', 
                        'header-ids', 
                        'link-patterns',
                        'html-classes',
                        'toc',

                    ]
                )
            except FileNotFoundError:
                raise HTTPNotFound(f'File Not Found: {given_path}')

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

