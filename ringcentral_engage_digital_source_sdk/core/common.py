__name__ = 'common'
__package__ = 'ringcentral_engage_digital_source_sdk.core'

import pydash as _
import sys, os
import json
from datetime import datetime
import importlib.util
from contextlib import contextmanager

def now():
  return str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def assign_module(src, ext):
  for key in dir(ext):
    if not _.strings.starts_with(key, '__'):
      setattr(src, key, getattr(ext, key))
  return src

@contextmanager
def add_to_path(p):
    old_path = sys.path
    sys.path = sys.path[:]
    sys.path.insert(0, p)
    try:
        yield
    finally:
        sys.path = old_path

def path_import(name, absolute_path):
  '''implementation taken from https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly'''
  with add_to_path(os.path.dirname(absolute_path)):
    spec = importlib.util.spec_from_file_location(name, absolute_path, submodule_search_locations=[])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def printError(e, type = ''):
  print(now(), type + ' error:')
  print(e)

def defaultEventHandler(event):
  return {
    'statusCode': 200,
    'body': json.dumps(event)
  }

def createResult(
  msg = '',
  status = 200,
  options = {}
):
  return _.assign({
    'statusCode': status,
    'body': msg or '',
  }, options)