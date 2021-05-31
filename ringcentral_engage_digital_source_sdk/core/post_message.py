from .sign import sign, parseDict
from requests import Request, Session

__name__ = 'post_message'
__package__ = 'ringcentral_engage_digital_source_sdk.core'

def postMessageToEngage (
  body,
  endpoint,
  secret = None
):

  '''* post message to channel real time url
  * @param {*} body // the post request body, js object
  * @param {*} endpoint // get the endpoint url from channel setting
  * @param {*} secret  // it is the api token from channel setting
  *
  * example body would be like:
  *
  {
    action: 'messages.create',
    params: {
      actions: ['show', 'reply'],
      id: '222888',
      body: 'hi there~',
      thread_id: '3423882',
      author: {
        id: 'uuu90u',
        firstname: 'John',
        lastname: 'Doe',
        screenname: 'John Doe',
        created_at: 123124323243
      }
    }
  }
  '''
  sig = sign(body, secret)
  headers = {
      'X-SMCCSDK-SIGNATURE': sig,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
  }
  data = parseDict(body)
  req = Request('POST', endpoint, data = data, json=None, headers = headers)
  prepared = req.prepare()
  s = Session()
  r = s.send(prepared)
  try:
    r.raise_for_status()
  except:
    raise Exception('HTTP status code: {0}\n\n{1}'.format(r.status_code, r.text))
  return r
