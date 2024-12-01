from .model		import *
from .timer		import Timer
from dataclasses	import dataclass

from PyQt6.QtWidgets	import QGraphicsItem, QGraphicsPixmapItem, QGraphicsRectItem
from PyQt6.QtGui	import QPixmap, QColor

class PixmapDB:
	def __init__(self):
		self.db = dict()
	def get(self, path : str) -> QPixmap:
		if path in self.db:
			return self.db[path]
		return self.add(path)
	def add(self, path):
		px = QPixmap(path)
		if px.isNull():
			raise FileNotFoundError(path)
		self.db[path] = px
		return px

pixmapDB = PixmapDB()

@dataclass(kw_only=True, init=False)
class Tile:
	pos		: Point
	spriteOffset	: Pointf
	gitem		: QGraphicsItem
	updated 	: bool
	size = None

	def __init__(self, pos=Point(0, 0)):
		self.gitem = None
		self.pos = pos
		self.spriteOffset = Pointf(0, 0)
		self.markUpdated()

	def setSpriteOffset(self, offset : Pointf = Pointf(0, 0)):
		self.spriteOffset = offset
		self.markUpdated()

	def needUpdate(self):
		return self.updated

	def markUpdated(self):
		self.updated = True
	
	def update(self) -> QGraphicsItem:
		self.updatePos()
		self.updated = False
		return self.gitem
		
	def updatePos(self):
		tsize = self.getTileSize()
		x = self.pos.x * tsize + self.spriteOffset.x * tsize
		y = self.pos.y * tsize + self.spriteOffset.y * tsize
		self.gitem.setPos(x, y)
		
	def setPos(self, pos : Point):
		self.updated = True
		self.pos = pos

	def moveByOffset(self, offset : Point):
		self.setPos(self.pos + offset)

	@classmethod
	def setTileSize(cls, size):
		cls.size = size
		
	@classmethod
	def getTileSize(cls):
		return cls.size

	def getGitem(self):
		return self.gitem

@dataclass(init=False)
class TilePixmap(Tile):
	pixmap	: QPixmap

	def __init__(self):
		super().__init__()
		self.desiredSize = None

	def setPixmap(self, path):
		self.pixmap = pixmapDB.get(path)
		self.markUpdated()

	def setDesiredSize(self, size : Point = None):
		self.desiredSize = size
		self.markUpdated()

	def update(self):
		if self.desiredSize:
			px = self.pixmap.scaled(self.desiredSize.x, self.desiredSize.y)
		else:
			px = self.pixmap
		self.gitem = QGraphicsPixmapItem(px)
		return super().update()

@dataclass(init=False)
class TileRect(Tile):
	color : str

	def __init__(self, pos : Point, color : str):
		super().__init__(pos=pos)
		self.setColor(color)

	def setColor(self, color : str):
		self.markUpdated()
		self.color = color

	def update(self):
		qc = QColor(self.color)
		tsize = self.getTileSize()
		self.gitem = QGraphicsRectItem(0, 0, tsize, tsize)
		self.gitem.setBrush(qc)
		self.gitem.setPen(QColor('black'))
		return super().update()
