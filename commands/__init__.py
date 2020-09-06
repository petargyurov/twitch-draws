PREFIX = "!"


def process(message):
	if message.startswith(PREFIX):
		return message[1:]
	return None