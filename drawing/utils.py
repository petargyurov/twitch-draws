from random import randint


def round_nearest(n, base):
	return base * round(n / base)


def clamp(n, smallest, largest):
	return max(smallest, min(n, largest))


def random_color():
	return '#{:02x}{:02x}{:02x}'.format(randint(0, 255),
										randint(0, 255),
										randint(0, 255))
