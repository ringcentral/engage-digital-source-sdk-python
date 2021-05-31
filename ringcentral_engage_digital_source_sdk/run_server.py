
name = 'ringcentral_engage_digital_source_sdk.run_server'

import os
from . import createApp
from dotenv import load_dotenv
load_dotenv()

def runServer(conf):
  port = os.environ['PORT'] or 9898
  host = os.environ['HOST'] or '127.0.0.1'
  app = createApp(conf)
  app.run(
    host=host,
    port=port,
    debug=True,
    load_dotenv=True
  )

