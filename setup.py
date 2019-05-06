#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Setup file for fb_duckling.

    This file was generated with PyScaffold 3.0.3.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: http://pyscaffold.org/
"""

import sys
from setuptools import setup

# Add here console scripts and other entry points in ini-style format
entry_points = """
[console_scripts]
# script_name = fb_duckling.module:function
# For example:
# fibonacci = fb_duckling.skeleton:run
"""


def setup_package():

    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=['pyscaffold>=2.5,<3.1a0'] + sphinx,
          entry_points=entry_points,
          use_pyscaffold=True,
          dependency_links=["https://github.com/facebook/duckling"])


if __name__ == "__main__":
    setup_package()
