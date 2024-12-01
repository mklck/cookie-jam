from .model		import Point, Deadplace
from .tile		import TilePixmap
from .entity		import Entity
from dataclasses	import dataclass
from typing		import List

class Paper(TilePixmap):
	pass

@dataclass(init=False)
class Map:
	background	: TilePixmap
	mainHero	: Entity
	deadplace	: List[Deadplace]
	paper		: List[Paper]
	def __init__(self, size : Point):
		self.size = size

	def setBackground(self, bg : TilePixmap):
		self.background = bg
	
	def setMainHero(self, e : Entity):
		self.mainHero = e

	def setDeadplace(self, d : list[Deadplace]):
		self.deadplace = d

	def setPapers(self, p : list[Paper]):
		self.paper = p

	def isPointDead(self, p : Point):
		if not self.isPointInMap(p):
			return True
		for x in self.deadplace:
			if p in x:
				return True
		return False
	def isPointInMap(self, p : Point):
		if p.x < 0 or p.y < 0:
			return False
		if p.x >= self.size.x or p.y >= self.size.y:
			return False
		return True
