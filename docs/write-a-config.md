# Write SDK source server config file

Check [../example_configs/demo_config.py](../example_configs/demo_config.py) as example.

```python

def onRequest(event):
  """
  req is parsed dict like this:
  {
    'pathParameters': {
      'action': action
    },
    'queryStringParameters': dict(request.args),
    'body': body if _.predicates.is_dict(body) else json.loads(body or '{}'),
    'headers': dict(request.headers)
  }
  """
  body = event['body']
  action = body['action']
  print('body:', body)
  print('action:', action)
  result = None
  # check https://github.com/ringcentral/engage-digital-source-sdk/wiki for more info
  if action == 'implementation.info':
      result = {
        'objects':
        {
          'messages': ['create', 'show', 'list'],
          'private_messages': ['create', 'show', 'list'],
          'threads': ['create', 'show', 'list']
        },
        'options': []
      }
  elif action == 'threads.list' or action == 'private_messages.list' or action == 'messages.list':
      result = []
  elif action == 'threads.show' or action == 'private_messages.show' or action == 'messages.show':
      result = ''
  else:
      result = {}
  print('result', result)
  return result

# extends or override routes as you need
def appExtend (app):
  @app.route('/test1', methods=['GET'])
  def onTest1():
    return {
      'statusCode': 200,
      'body': 'test1'
    }
```
