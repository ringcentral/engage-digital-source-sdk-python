name = 'ringcentral_engage_digital_source_sdk.app'

from flask import Flask, request, jsonify
import pydash as _
from .core.flask_request_parser import flaskRequestParser
from dotenv import load_dotenv
load_dotenv()
import os, sys
from .core.common import createResult
from .core.sign import sigValid, sign, parseDict

def initApp(conf):
  home = '/'
  noRoute = False
  env = 'devtest'
  try:
    home = os.environ['SERVER_HOME']
    noRoute = os.environ['NO_ROUTE'] or False
    env = os.environ['FLASK_ENV'] or 'devtest'
  except:
    pass

  app = Flask(env)

  @app.route('/test', methods=['GET'])
  def index():
    return 'RingCentral engage source SDK server running'
  @app.route('/favicon.ico', methods=['GET'])
  def favicon():
    return ''

  if noRoute:
    pass
  else:
    @app.route(home, methods=['POST'])
    def onRequest():
      event = flaskRequestParser(request, home)
      app.logger.warning(event)
      valid = sigValid(event)
      if not valid:
        return 'not valid', 422
      resp = conf.onRequest(event)
      sig = sign(resp)
      headers = {
        'Content-Type': 'application/json',
        'X-SMCCSDK-SIGNATURE': sig
      }
      data = parseDict(resp)
      return data, 200, headers

  if not conf.appExtend is None:
    conf.appExtend(app)

  return app
  # app.run(
  #   host=host,
  #   port=port,
  #   debug=True,
  #   load_dotenv=True
  # )

