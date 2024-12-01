from .tile		import Tile
from PyQt6.QtWidgets	import QGraphicsScene

class Scene(QGraphicsScene):
	def __init__(self):
		super().__init__()
		self.tiles = list()

	def addItem(self, t : Tile):
		self.tiles.append(t)
		qg = t.update()
		super().addItem(qg)

	def addQtItem(self, q):
		super().addItem(q)

	def updateAll(self):
		for t in self.tiles:
			if not t.needUpdate():
				continue
			self.updateTile(t)

	def updateTile(self, t : Tile):
		self.removeItem(t.getGitem())
		self.addItem(t)
