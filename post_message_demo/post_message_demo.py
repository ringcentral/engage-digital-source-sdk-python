import os

from dotenv import load_dotenv
load_dotenv()

from ringcentral_engage_digital_source_sdk import postMessageToEngage
from datetime import datetime
import string
import random

def uid ():
  letters = string.ascii_lowercase
  return ''.join(random.choice(letters) for i in range(10))

def main ():
  url = ''
  body = {
    'action': 'messages.create',
    'params': {
      'actions': ['show', 'reply'],
      'id': uid(),
      'body': 'hi there~' + uid(),
      'thread_id': uid(),
      'author': {
        'id': uid(),
        'firstname': 'John',
        'lastname': 'Doe',
        'screenname': 'John Doe',
        'created_at': 1622426621537
      }
    }
  }
  token = ''
  try:
    url = os.environ['RINGCENTRAL_ENGAGE_DIGITAL_ENDPOINT']
    token = os.environ['RINGCENTRAL_ENGAGE_DIGITAL_API_TOKEN']
  except:
    pass
  r = postMessageToEngage(body, url, token)
  print('result', r)

main()