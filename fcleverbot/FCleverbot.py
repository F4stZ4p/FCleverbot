import aiohttp
import asyncio

class FCleverbot:
	def __init__(self, cs=None, api_user=None, api_key=None, nick=None):
		self.api_user = api_user
		self.api_key = api_key
		self.nick = nick

		if self.api_user is None or self.api_key is None:
			raise Exception("API user or key is missing. FCleverbot will not work. Get one at https://cleverbot.io")

		if self.nick is None:
			raise Exception("Nick not specified.")

		if not cs:
			self.cs = aiohttp.ClientSession()

		else:
			self.cs = cs

	async def close(self):
		"""Close client session"""
		await self.cs.close()

	async def talk(self, content):
		"""Talk to Cleverbot (only response)"""
		params = {
			"user": self.api_user,
			"key": self.api_key,
			"nick": self.nick,
			"text": content
		}
		async with self.cs.post("https://cleverbot.io/1.0/ask", data=params) as conversation:
			data = await conversation.json()
			return data["response"]

	async def talkjson(self, content):
		"""Talk to Cleverbot (full json)"""
		params = {
			"user": self.api_user,
			"key": self.api_key,
			"nick": self.nick,
			"text": content
		}
		async with self.cs.post("https://cleverbot.io/1.0/ask", data=params) as conversation:
			data = await conversation.json()
			return data