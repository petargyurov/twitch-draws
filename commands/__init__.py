PREFIX = "!"
COMMANDS = {
	'draw': (int, int, str)
}


def validate(command):
	parts = command.split(' ')
	cmd = parts[0]
	if not COMMANDS.get(cmd):
		raise KeyError

	args = parts[1:]
	spec = COMMANDS.get(cmd)
	if len(args) != len(spec):
		raise TypeError
	for i, s in enumerate(spec):
		args[i] = s(args[i])  # will raise ValueError if it cannot cast

	return cmd, args


def process(message):
	if not message.startswith(PREFIX):
		return None
	command = message[1:]

	command, args = validate(command)
	return command, args