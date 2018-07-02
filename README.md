# FCleverbot
An asynchronous CleverbotIO Python libary

# Installation
Requires Python 3.5 or above and aiohttp

`pip install -U git+https://github.com/f4stz4p/fcleverbot`

# Usage
```python
# Getting clear response
import fcleverbot
fc = fcleverbot.FCleverbot(api_user="your api user key", api_key="your api key", nick="your nick")
return await fc.talk("hi")

# Getting all json
import fcleverbot
fc = fcleverbot.FCleverbot(api_user="your api user key", api_key="your api key", nick="your nick")
return await fc.talkjson("hi")
```
