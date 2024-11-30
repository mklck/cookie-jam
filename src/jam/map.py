from .model	import Point
from .tile	import TilePixmap
from .entity	import Entity

class Map:
	def __init__(self, size : Point):
		self.size = size

	def setBackground(self, bg : TilePixmap):
		self.background = bg
	
	def setMainHero(self, e : Entity):
		self.mainHero = e

	def isPointInMap(self, p : Point):
		if p.x < 0 or p.y < 0:
			return False
		if p.x >= self.size.x or p.y >= self.size.y:
			return False
		return True
