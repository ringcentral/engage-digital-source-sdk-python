
name = 'ringcentral_engage_digital_source_sdk.rces'

import argparse
import os
from .run_server import runServer
from os.path import dirname, realpath, join, isabs
import pydash as _
import sys
from .core.common import path_import

def main():
  cwd = os.getcwd()
  parser = argparse.ArgumentParser(
    description='''
Cli tool to run RingCentral Engage source SDK server.
Example: rces config.py
With envs: PORT=9800 HOST=127.0.0.1 rces config.py
    '''
  )
  parser.add_argument(
    'path',
    metavar='p',
    help='config file path name like config.py'
  )

  try:
    args = parser.parse_args()
  except:
    return parser.print_help()

  if not _.predicates.is_string(
    _.get(args, 'path')
  ):
    parser.print_help()
  else:
    p = args.path
    if not isabs(p):
      p = join(cwd, p)
    conf = path_import('ringcentral_engage_digital_source_sdk.localConfig', p)
    runServer(conf)
