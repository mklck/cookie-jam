from .map		import Map
from .model		import *
from .entity		import Entity
from .tile		import *
from .gui		import *
from dataclasses	import dataclass, field

class MapPainter(Map):
	def __init__(self, size : Point):
		Tile.setTileSize(80)
		winSize = Point(
			Tile.size * size.x,
			Tile.size * size.y
		)
		self.window = Window(winSize)
		self.scene = self.window.getScene()
		super().__init__(size)

	def show(self):
		self.initScene()
		self.window.show(self.update)

	def update(self, obj = None):
		if type(obj) is QKeyEvent:
			self.handleKeyboard(obj.text())
		self.scene.updateAll()

	def initScene(self):
		for tr in self.grid:
			if ((tr.pos.x % 2) == (tr.pos.y % 2)):
				tr.setColor("#b123b7")
			self.addTile(tr)
		self.addTile(self.mainHero)

	def handleKeyboard(self, key : str):
		movements = {
			'w': Point(0, -1),
			's': Point(0,  1),
			'd': Point(1,  0),
			'a': Point(-1, 0),
		}
		if key not in movements:
			return
		self.mainHero.moveByOffset(movements[key])

	def addTile(self, t : Tile):
		self.scene.addItem(t)

	def tileIterate(self):
		return self.size.iterate()
