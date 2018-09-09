import re
from os.path import join, dirname
from setuptools import setup, find_packages

# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'wikibox', '__init__.py')) as v_file:
    package_version = re.compile(r'.*__version__ = \'(.*?)\'', re.S) \
        .match(v_file.read()) \
        .group(1)


dependencies = [
    'mako',
    'nanohttp >= 1.5',
    'gunicorn',
    'markdown2',
    'pygments',
]


setup(
    name='wikibox',
    version=package_version,
    author='Netalic',
    author_email='vahid.mardani@gmail.com',
    install_requires=dependencies,
    packages=find_packages('.', exclude=['*.tests']),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'wikibox = wikibox.cli:main'
        ]
    },
)

