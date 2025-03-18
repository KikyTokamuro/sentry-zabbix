# coding: utf-8
"""
sentry_zabbix
"""
from __future__ import absolute_import
from importlib.metadata import version

try:
    VERSION = version(__name__)
except Exception as e:
    VERSION = 'unknown'

from sentry.plugins.base import register
from .plugin import ZabbixPlugin

# register(ZabbixPlugin)
