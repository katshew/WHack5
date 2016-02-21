# -*- coding: utf-8 -*-

"""Treat yaklient as package"""

import config
import settings
from objects.location import Location
from objects.user import NoBasecampSetError, TooCloseToSchoolException
from objects.user import User

__title__ = 'yaklient'
__author__ = 'Akash Levy'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Akash Levy'
__version__ = '2.6.3'
