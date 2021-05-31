# Direct use, no CLI

You can certainly use it as a module instead of a CLI tool.

Check [src/ringcentral_engage_digital_source_sdk/run_server.py](../ringcentral_engage_digital_source_sdk/run_server.py)

## For nodejs server

```python
from ringcentral_engage_digital_source_sdk import createApp

def runServer(conf):
  port = 9898
  host = '127.0.0.1'
  app = createApp(conf)
  app.run(
    host=host,
    port=port,
    debug=True,
    load_dotenv=True
  )

```

## For AWS Lambda

```js
import { createApp } from 'ringcentral-engage-source'

const path = './auto-reply-all.js'
console.log('-> bot:', path)
const conf = require(path)
const app = createApp(conf)

export default app

```
