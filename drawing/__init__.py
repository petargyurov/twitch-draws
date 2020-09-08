import turtle
from random import choice
from .utils import round_nearest


class Artist(object):
	def __init__(self, grid_size, pen_speed=0, colormode=255):
		self.width = 1000
		self.height = 1000
		self.grid_size = grid_size
		self.speed = pen_speed
		self.colormode = colormode

		self.screen = turtle.Screen()
		self.screen.setup(self.width, self.height)
		self.screen.setworldcoordinates(0, 0, self.width, self.height)
		self.screen.colormode(self.colormode)

		self.pen = turtle.Turtle()
		self.pen.speed(self.speed)
		self.grid_pen = self.pen.clone()
		self.grid_pen.hideturtle()
		self.pen.hideturtle()

	def draw_grid(self, color=(190, 190, 190)):
		r, g, b = color
		self.grid_pen.color(r, g, b)

		steps_x = int(self.width / self.grid_size)
		steps_y = int(self.height / self.grid_size)
		self.grid_pen.home()

		# draw vertical lines
		for x in range(0, self.width + 1, steps_x):
			self.grid_pen.up()
			self.grid_pen.goto(x, 0)
			self.grid_pen.down()
			self.grid_pen.goto(x, self.height)

		# draw horizontal lines
		for y in range(0, self.height + 1, steps_y):
			self.grid_pen.up()
			self.grid_pen.goto(0, y)
			self.grid_pen.down()
			self.grid_pen.goto(self.width, y)

	def draw(self, x, y):
		# normalise given coords
		steps_x = int(self.width / self.grid_size)
		x = round_nearest(x, steps_x)
		steps_y = int(self.height / self.grid_size)
		y = round_nearest(y, steps_y)

		self.pen.shape("square")
		self.pen.resizemode("user")
		size = (1 / self.grid_size) * 50  # TODO: magic number?
		position_offset = size * 10
		self.pen.shapesize(size, size)
		self.pen.up()

		self.pen.goto(x+position_offset, y+position_offset)  # TODO: normalise to valid coords
		self.pen.stamp()
		self.pen.down()

	def _simulate(self, n): # TODO: remove after testing
		self.pen.shape("square")
		self.pen.resizemode("user")
		size = (1 / self.grid_size) * 50  # TODO: magic number?
		position_offset = size * 10
		self.pen.shapesize(size, size)
		self.pen.up()

		steps_x = int(self.width / self.grid_size)
		steps_y = int(self.height / self.grid_size)
		for i in range(0, n):
			x = choice(range(0, self.width, steps_x)) + position_offset
			y = choice(range(0, self.height, steps_y)) + position_offset
			self.pen.goto(x, y)
			self.pen.color(choice(["green", "red", "blue", "magenta"]))
			self.pen.stamp()

	def clear_grid(self):
		self.grid_pen.clear()

	def save_image(self, filename):
		self.screen.getcanvas().postscript(file=f"{filename}.eps")
