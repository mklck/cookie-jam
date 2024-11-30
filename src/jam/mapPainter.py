from .map		import Map
from .model		import *
from .entity		import Entity
from .tile		import *
from .gui		import *
from .animator		import Animator
from .controller	import Controller
from dataclasses	import dataclass, field

class MapPainter(Map):
	def __init__(self, size : Point):
		Tile.setTileSize(80)
		winSize = Point(
			Tile.size * size.x,
			Tile.size * size.y
		)
		self.controller = Controller(self)
		self.window = Window(winSize)
		self.scene = self.window.getScene()
		super().__init__(size)

	def show(self):
		self.initScene()
		self.window.show(self.update)

	def update(self, obj = None):
		if type(obj) is QKeyEvent:
			self.controller.keyEvent(obj.text())
		self.controller.step()
		self.scene.updateAll()

	def initScene(self):
		self.addTile(self.background)
		self.addTile(self.mainHero)

	def addTile(self, t : Tile):
		self.scene.addItem(t)
