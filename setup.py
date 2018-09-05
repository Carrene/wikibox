import re
from os.path import join, dirname
from setuptools import setup, find_packages
from Cython.Build import cythonize

# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'wikibox', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S) \
        .match(v_file.read()) \
        .group(1)

dependencies = [
    'restfulpy >= 1.9.0',
    'oathcy >= 1.3.0',
    'pycrypto',

    # deployment
    'gunicorn',
]


# FIXME: Uncomment it before deploy
#wikibox_modules = cythonize(
#    'wikibox/**/*.pyx',
#    compiler_directives={'linetrace': True}
#)


setup(
    name="wikibox",
    version=package_version,
    author="Netalic",
    author_email="mt@netalic.de",
    install_requires=dependencies,
    packages=find_packages('.', exclude=['*.tests']),
    include_package_data=True,
    # FIXME: Uncomment it before deploy
    #ext_modules=wikibox_modules,
    test_suite="wikibox.tests",
    entry_points={
        'console_scripts': [
            'wikibox = wikibox:wikibox.cli_main',
        ]
    }
)

