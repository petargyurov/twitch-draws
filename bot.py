"""
Mostly adapted from: https://github.com/Carberra/twitch-bot-tutorial

"""

from irc.bot import SingleServerIRCBot
from requests import get

from commands import process
from config import *


class Bot(SingleServerIRCBot):
	def __init__(self, artist):
		self.artist = artist
		self.HOST = "irc.chat.twitch.tv"
		self.PORT = 6667
		self.USERNAME = USERNAME.lower()
		self.CLIENT_ID = CLIENT_ID
		self.TOKEN = OAUTH_TOKEN
		self.CHANNEL = f"#{OWNER}"

		url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
		headers = {"Client-ID": self.CLIENT_ID,
				   "Accept"   : "application/vnd.twitchtv.v5+json"}
		response = get(url, headers=headers)  # TODO: handle bad responses
		super().__init__([(self.HOST, self.PORT, f"oauth:{self.TOKEN}")],
						 self.USERNAME, self.USERNAME)

	def on_welcome(self, conn, event):
		for req in ("membership", "tags", "commands"):
			conn.cap("REQ",
					 f":twitch.tv/{req}")  # TODO: handle any errors here?

		conn.join(self.CHANNEL)
		self.send_message("=== BOT IS ONLINE ===")

	def on_pubmsg(self, conn, event):
		tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
		user = {"name": tags["display-name"], "id": tags["user-id"]}
		message = event.arguments[0]

		command = None
		try:
			command, args = process(message)
		except (KeyError, TypeError, ValueError) as e:
			pass

		if command:
			print(f"{user['name']}: {command} {args}")
			handler = getattr(self.artist, command)
			if handler and callable(handler):
				handler(*args)

	def send_message(self, message):
		self.connection.privmsg(self.CHANNEL, message)
