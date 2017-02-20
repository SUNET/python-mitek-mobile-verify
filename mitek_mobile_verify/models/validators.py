# -*- coding: utf-8 -*-

import six
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

__author__ = 'lundberg'


def is_string(s):
    if s is None or isinstance(s, six.string_types) or isinstance(s, bytes):
        # Apparently bytes needs to go in the KeyValueOfstringstring structure
        return True
    logger.error('{} {} not string or bytes'.format(type(s), s))
    return False


def is_bool(b):
    if b is None or isinstance(b, bool):
        return True
    logger.error('{} {} not bool'.format(type(b), b))
    return False


def is_datetime(dt):
    if isinstance(dt, datetime):
        return True
    logger.error('{} {} not datetime'.format(type(dt), dt))
    return False


def is_string_value_list(l):
    """
    :param l: Data structure
    :type l: list
    :return: True|False
    :rtype: bool

    Check if the dict is compatible with SOAP type ArrayOfstring.
    """
    if l is None or isinstance(l, list) and all([is_string(item) for item in l]):
        return True
    return False


def is_string_value_dict(d):
    """
    :param d: Data structure
    :type d: dict
    :return: True|False
    :rtype: bool

    Check if the dict is compatible with SOAP type KeyValueOfstringstring.
    """
    if d is None or all([is_string(v) for v in d.values()]):
        return True
    return False
