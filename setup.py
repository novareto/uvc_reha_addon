# !/usr/bin/env python

import codecs
import os
import re

from distutils.core import setup
from setuptools import setup


PACKAGES = []
INSTALL_REQUIRES = []


with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name={{ cookiecutter.project_slug }},
    packages=PACKAGES,
    version={{ cookiecutter.version }},
    description={{ cookiecutter.project_short_description }},
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author={{ cookiecutter.full_name.replace('\"', '\\\"') }},
    license={{ cookiecutter.license }},
    author_email={{ cookiecutter.email }},
    url=https://git.bg-kooperation.de,
)
