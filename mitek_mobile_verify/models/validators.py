# -*- coding: utf-8 -*-

import six
import base64
from datetime import datetime

__author__ = 'lundberg'


def is_string(s):
    if s is None or isinstance(s, six.string_types):
        return True
    return False


def is_bool(b):
    if b is None or isinstance(b, bool):
        return True
    return False


def is_base64(s):
    enc = base64.b64encode(base64.b64decode(s))
    if enc == s:
        return True
    return False


def is_datetime(dt):
    if isinstance(dt, datetime):
        return True
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
