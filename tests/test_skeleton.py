#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from fb_duckling.skeleton import fib

__author__ = "Benjamin Breton"
__copyright__ = "Benjamin Breton"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
