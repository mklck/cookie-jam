from .model	import Point
from .tile	import TileRect
from .entity	import Entity
from itertools	import product

class Map:
	def __init__(self, size : Point, default_colour="white"):
		self.size = size
		self.grid = []
		self.entities = []
		for p in size.iterate():
			tr = TileRect(pos=p, color=default_colour)
			self.grid.append(tr)
	
	def setMainHero(self, e : Entity):
		self.mainHero = e
