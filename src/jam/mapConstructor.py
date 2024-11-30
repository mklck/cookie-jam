import json5
from typing	import List

from .map	import Map
from .tile	import TilePixmap
from .entity	import Entity
from .textures	import textureManager
from .model	import Point, Deadplace

class MapConstructor:
	def feedJSON(self, path : str):
		with open(path, 'r') as f:
			self.data = json5.load(f)

	def readMapSize(self) -> Point:
		size = self.data['size']
		return Point(*size)

	def getMap(self) -> Map:
		size = self.readMapSize()
		m = Map(size)
		m.setMainHero(self.readHero())

		pixmap = self.readBackground()
		m.setBackground(pixmap)
		m.setDeadplace(self.readDeadplace())
		return m

	def readBackground(self) -> TilePixmap:
		mapSize = self.readMapSize()
		tsize = self.readTileSize()

		desiredSize = mapSize * tsize
		pixmap = TilePixmap()
		pixmap.setPixmap(self.data['background'])
		pixmap.setDesiredSize(desiredSize)
		return pixmap
	def readHero(self) -> Entity:
		tsize = self.readTileSize()
		e = Entity(textureManager)
		e.setDesiredSize(Point(tsize, tsize))
		startPos = self.data['startPos']
		startPos = Point(*startPos)
		e.setPos(startPos)
		return e

	def readTileSize(self) -> int:
		return self.data['tileSize']

	def readDeadplace(self) -> List[Deadplace]:
		d = self.data["deadplaces"]
		deadplaces = []
		for x in d:
			start, end = x
			start = Point(*start)
			end = Point(*end)
			deadplaces.append(Deadplace(start=start, end=end))
		return deadplaces
