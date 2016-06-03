#!/usr/bin/env python

from setuptools import setup
from subprocess import check_output

version = check_output(['git', 'describe', '--tags']).strip('\n')

url = 'https://github.com/matterport/andandand'

setup(
    name='andandand',
    version=version,
    author='Teran McKinney',
    author_email='sega01@go-beyond.org',
    description='HTTP/S health check proxy to test multiple health checks.',
    keywords=['http', 'health'],
    license='Unlicense',
    url=url,
    packages=['andandand'],
    setup_requires=[
        'flake8'
    ]
)
