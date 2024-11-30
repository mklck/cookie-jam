from .map		import Map
from .model		import *
from .entity		import Entity
from .tile		import *
from .gui		import *
from .animator		import Animator
from dataclasses	import dataclass, field

class MapPainter(Map):
	def __init__(self, size : Point):
		Tile.setTileSize(80)
		winSize = Point(
			Tile.size * size.x,
			Tile.size * size.y
		)
		self.animator = Animator()
		self.window = Window(winSize)
		self.scene = self.window.getScene()
		super().__init__(size)

	def show(self):
		self.initScene()
		self.window.show(self.update)

	def update(self, obj = None):
		if type(obj) is QKeyEvent:
			self.handleKeyboard(obj.text())
		self.animator.step()
		self.scene.updateAll()

	def initScene(self):
		for tr in self.grid:
			if ((tr.pos.x % 2) == (tr.pos.y % 2)):
				tr.setColor("#b123b7")
			self.addTile(tr)
		self.addTile(self.mainHero)

	def handleKeyboard(self, key : str):
		movements = {
			'w': 'north',
			's': 'south',
			'a': 'west',
			'd': 'east',
		}
		if key not in movements:
			return
		direction = movements[key]
		self.animator.animate(self.mainHero, direction)

	def addTile(self, t : Tile):
		self.scene.addItem(t)

	def tileIterate(self):
		return self.size.iterate()
