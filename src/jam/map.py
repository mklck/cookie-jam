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
