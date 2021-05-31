"""
config module, load user config.py to extend default config
"""

name = 'ringcentral_engage_digital_source_sdk.config'

import os
from os.path import dirname, realpath, join
from .core.common import assign_module, path_import, printError

def initConfig(conf):
  configAll = None
  try:
    dirPath = dirname(realpath(__file__))
    configPath = join(dirPath, 'core/config_default.py')
    defaultConfig = path_import('ringcentral_engage_digital_source_sdk.core.defaultConfig', configPath)
    configAll = defaultConfig
    configAll = assign_module(configAll, conf)
    return configAll
  except Exception as e:
    printError(e)

  return configAll