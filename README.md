# [RingCentral Engage digital source SDK python](https://github.com/ringcentral/engage-digital-source-sdk-python)

Framework(python) to create `Engage Digital channel SDK` channel for RingCentral Engage Digital. [Wiki about RingCentral Engage Digital channel SDK channel](https://github.com/ringcentral/engage-digital-source-sdk/wiki), which is a customized channel that support any source user want to use.

### Install Prerequisites

- Python3.6+ and Pip3.
- First we install [virtualenv](https://virtualenv.pypa.io/en/latest/) which will create an isolated environment in which to install and run all the python libraries needed by this framework. Using virtualenv will ensure that the libraries installed for this project do not conflict or disrupt the other python projects you are working on.
- RingCentral Engage(Dimelo) account, [request a demo](https://www.ringcentral.com/digital-customer-engagement.html).

## Quick start

Let's start a simple RingCentral Engage source server.

```bash
# init project
bin/init
source venv/bin/activate
```

Next, we need to run [ngrok](https://ngrok.com/), a tool for routing web requests to a localhost. This is what will allow your local bot in development to receive webhooks from RingCentral. ngrok is a node app and is installed and start as follows:

```bash
./bin/proxy

# will show
Forwarding                    https://xxxx.ap.ngrok.io -> localhost:9898
# Remember the https://xxxx.ap.ngrok.io, we will use it later
```

Follow [Step by step guide to create Dimelo SDK source in Admin console](https://github.com/ringcentral/engage-digital-source-sdk-js/blob/master/docs/enable-sdk-source.md) to prepare the source.

```bash
# create env file
cp .env.sample .env
# then edit .env, set proper setting according to the tip in .env

# run local dev server
./bin/start
```

### Test source server

Save your source, your server will get request, you check the request log from console.

## Use it as CLI tool

```bash
pip3 install ringcentral_engage_digital_source_sdk
rces path/to/config_file.py
```

## Use is as a module

[docs/direct-use.md](docs/direct-use.md)

## Post message to channel

You can get channel realtime url and api token from channel setting page, post new message to the channel.

Check [post_message_demo/post_message_demo.py](post_message_demo/post_message_demo.py) as an example.

```python

from ringcentral_engage_digital_source_sdk import postMessageToEngage

def main ():
  url = 'RINGCENTRAL_ENGAGE_DIGITAL_ENDPOINT'
  token = 'RINGCENTRAL_ENGAGE_DIGITAL_API_TOKEN'
  body = {
    'action': 'messages.create',
    'params': {
      'actions': ['show', 'reply'],
      'id': 'xxxxx',
      'body': 'hi there~',
      'thread_id': 'yyyyy',
      'author': {
        'id': 'zzzzz',
        'firstname': 'John',
        'lastname': 'Doe',
        'screenname': 'John Doe',
        'created_at': 1622426621537
      }
    }
  }
  r = postMessageToEngage(body, url, token)
  print('result', r)

```

## Write a config

[docs/write-a-config.md](docs/write-a-config.md)

## Build and Deploy to AWS Lambda

todo

## Init a source server project with factory CLI tool

todo

## License

MIT
