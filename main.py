from bot import start_bot
from drawing import start_drawing
import threading


if __name__ == '__main__':
	# start bot on a separate thread
	bot_thread = threading.Thread(target=start_bot, daemon=False)
	bot_thread.start()

	# drawing has to be done on the main thread
	start_drawing()