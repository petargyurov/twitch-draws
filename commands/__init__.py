from .cmds import up, down, left, right


PREFIX = "!"
COMMANDS = {
	"up": up,
	"down": down,
	"left": left,
	"right": right
}


def _process(message):
	if message.startswith(PREFIX):
		return message[1:]
	return None


def perform(user, command, pen):
	command = _process(command)
	func = COMMANDS.get(command)
	if func:
		func(pen)