#!/usr/bin/env python

"""The setup script."""

import codecs
import os
import re

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('docs/HISTORY.rst') as history_file:
    history = history_file.read()

requirements = "" 

setup_requirements = "" 

setup(
    name="{{ cookiecutter.project_slug }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    url="https://git.bg-kooperation.de",
    entry_points={
        'docmanager.plugin': 'target=uvcsite',
    },
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    setup_requires=setup_requirements,
    test_suite='tests',
    zip_safe=False,
)
