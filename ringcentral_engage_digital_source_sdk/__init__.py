
name = 'ringcentral_engage_digital_source_sdk'

from .app import initApp
from .config import initConfig
from .core.post_message import *
from .core.sign import *

def createApp(config):
  conf = initConfig(config)
  app1 = initApp(conf)
  return app1

