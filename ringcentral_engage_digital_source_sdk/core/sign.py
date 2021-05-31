
import hmac
import pydash as _
import os
import json
import hashlib

__name__ = 'sign'
__package__ = 'ringcentral_engage_digital_source_sdk.core'

def parseDict (body):
  data = json.dumps(body, separators=(',', ':'))
  return data.encode('utf-8')

def sign(
  _str = '',
  secret = os.environ['RINGCENTRAL_ENGAGE_DIGITAL_API_TOKEN']
):
  str1 = json.dumps(_str, separators=(',', ':')) if _.predicates.is_dict(_str) or _.predicates.is_list(_str) else _str
  encoded=str1.encode('utf-8')
  keyCoded = secret.encode('utf-8')
  sign = hmac.new(keyCoded, encoded, hashlib.sha512).hexdigest()
  return sign

def verify(body, signature, secret):
  noSign = None
  try:
    noSign = os.environ['NO_SIGN_CHECK']
  except:
    pass
  if not noSign is None:
    return True
  return sign(body, secret) == signature

def sigValid (event):
  sig = event['headers']['x-smccsdk-signature']
  if sig is None:
    return False
  return verify(
      event['body'],
      sig,
      os.environ['RINGCENTRAL_ENGAGE_DIGITAL_API_TOKEN']
    )
