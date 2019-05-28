# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'

from .utils import get_default_locale, get_default_url, get_default_port
from .base_class import BaseClass
from .duckling import Duckling
from .anonymizer import Anonymizer
