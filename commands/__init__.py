from .cmds import up


PREFIX = "!"
COMMANDS = {
	"up": up
}


def _process(message):
	if message.startswith(PREFIX):
		return message[1:]
	return None


def perform(user, command, pen):
	command = _process(command)
	func = COMMANDS.get(command)
	print(f"Performing <{command}>")
	func(pen)