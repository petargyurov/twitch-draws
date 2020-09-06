from bot import Bot
from drawing import Artist
import threading
from models import create_all
import turtle


def start_bot(artist):
	bot = Bot(artist)
	bot.start()


if __name__ == '__main__':
	create_all()

	artist = Artist(10)
	artist.draw_grid()

	# start bot on a separate thread
	bot_thread = threading.Thread(target=start_bot, args=(artist,), daemon=False)
	bot_thread.start()

	# drawing has to be done on the main thread
	turtle.done()
