'''
parse flask request to event format
'''

from urllib.parse import parse_qs, urlencode
import json
import pydash as _

def lower_dict_keys(some_dict):
    """Convert all keys to lowercase"""
    result = {}
    for key, value in some_dict.items():
        try:
            result[key.lower()] = value
        except AttributeError:
            result[key] = value
    return result

def flaskRequestParser(request, action):
  '''
  parse flask request to event format:
  {
    'pathParameters': {
      'action': action
    },
    'queryStringParameters': dict(request.args),
    'body': body if _.predicates.is_dict(body) else json.loads(body or '{}'),
    'headers': dict(request.headers)
  }
  '''
  body = request.data
  if not body and request.form:
    body = urlencode(request.form)
    body = parse_qs(body)
  elif not body:
    try:
      body = request.json
    except:
      pass
  return {
    'pathParameters': {
      'action': action
    },
    'queryStringParameters': dict(request.args),
    'body': body if _.predicates.is_dict(body) else json.loads(body or '{}'),
    'headers': lower_dict_keys(dict(request.headers))
  }