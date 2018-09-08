

import sys
from os import chdir
from os.path import relpath, basename

from nanohttp import quickstart

import wikibox
from .configuration import configure, settings



DEFAULT_ADDRESS = '8080'


def parse_arguments(argv=None):
    import argparse

    argv = argv or sys.argv

    parser = argparse.ArgumentParser(prog=basename(argv[0]))
    parser.add_argument(
        '-c',
        '--config-file',
        action='append',
        default=[],
        dest='config_files',
        help='This option may be passed multiple times.'
    )

    parser.add_argument(
        '-b',
        '--bind',
        default=DEFAULT_ADDRESS,
        metavar='{HOST:}PORT',
        help='Bind Address. default: %s' % DEFAULT_ADDRESS
    )

    parser.add_argument(
        '-C',
        '--directory',
        default='.',
        help='Change to this path before starting the server default is: `.`'
    )

    parser.add_argument(
        '-V',
        '--version',
        default=False,
        action='store_true',
        help='Show the version.'
    )

    return parser.parse_args(argv[1:])


def main(argv=None):
    args = parse_arguments(argv=argv)

    if args.version:
        print(wikibox.__version__)
        return 0

    try:
        host, port = args.bind.split(':')\
            if ':' in args.bind else ('', args.bind)

        # Change dir
        if relpath(args.directory, '.') != '.':
            chdir(args.directory)

        configure(force=True)

        for f in args.config_files:
            settings.load_file(f)

        quickstart(
            application=wikibox.WikiBox(),
            host=host,
            port=int(port)
        )
    except KeyboardInterrupt:
        print('CTRL+C detected.')
        return -1
    else:
        return 0

