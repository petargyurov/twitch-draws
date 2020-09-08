

def round_nearest(n, base):
	return base * round(n/base)


def clamp(n, smallest, largest):
	return max(smallest, min(n, largest))
