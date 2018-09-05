
from nanohttp import settings, configure as nanohttp_configure


BUILTIN_CONFIGURATION = '''

root: /

'''


def configure(config=None, files=None, context=None, force=False):
    context = context or {}
    nanohttp_configure(
        context=context,
        force=force
    )
    settings.merge(BUILTIN_CONFIGURATION)

    if config:
        settings.merge(config)

    if files:
        for f in files:
            settings.load_files(f)

