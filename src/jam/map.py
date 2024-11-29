from .tile	import Tile
from .model	import Point
from itertools	import product

class Map:
	def __init__(self, size : Point, default_colour="white"):
		self.size = size
		self.grid =[[Tile() for _ in range(size.x)] for _ in range(size.y)]

	def setTileColour(self, p : Point, colour):
		t = self.getTile(p)
		t.colour = colour

	def validPoint(self, p : Point):
		cond0 = 0 <= p.x < self.size.x
		cond1 = 0 <= p.y < self.size.y
		return cond0 and cond1

	def getTile(self, p : Point):
		if not self.validPoint(p):
			raise IndexError(f"Invalid position {p}")
		return self.grid[p.x][p.y]

	def everyTilePoint(self):
		for x, y in product(range(self.size.x), range(self.size.y)):
			yield Point(x, y)

