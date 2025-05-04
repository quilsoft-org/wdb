import codecs
import re
import sys
import logging
from json import loads, dumps, JSONEncoder, JSONDecodeError
from urllib.parse import quote
from html import escape
from socketserver import TCPServer
from collections import OrderedDict
from io import StringIO
from multiprocessing.connection import Client as Socket
from importlib.util import find_spec
from importlib import import_module

logger = logging.getLogger  # o reemplazá si log_colorizer está disponible

def execute(cmd, globals_, locals_):
    exec(cmd, globals_, locals_)

def _detect_encoding(filename):
    import linecache
    lines = linecache.getlines(filename)
    return _detect_lines_encoding(lines)

_cookie_search = re.compile(r"coding[:=]\s*([-\w.]+)").search

def _detect_lines_encoding(lines):
    if not lines or lines[0].startswith("\xef\xbb\xbf"):
        return "utf-8"
    magic = _cookie_search("".join(lines[:2]))
    if magic is None:
        return 'utf-8'
    encoding = magic.group(1)
    try:
        codecs.lookup(encoding)
    except LookupError:
        return 'utf-8'
    return encoding

def to_unicode(string):
    return string

def to_unicode_string(string, filename):
    return string

def to_bytes(string):
    return string.encode('utf-8')

def from_bytes(bytes_):
    return bytes_.decode('utf-8')

def force_bytes(bytes_):
    if isinstance(bytes_, str):
        return bytes_.encode('utf-8')
    return bytes_

def is_str(string):
    return isinstance(string, (str, bytes))

def u(s):
    return s

def existing_module(module):
    return bool(find_spec(module))
