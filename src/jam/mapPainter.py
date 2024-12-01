from .map		import Map
from .model		import Point
from .tile		import Tile
from .gui		import MainWindowConstructor, KbdEvent
from .controller	import Controller
from .scene		import Scene

class MapPainter:
	def __init__(self, size : Point, tileSize : int):
		Tile.setTileSize(tileSize)
		winSize = Point(
			tileSize * size.x,
			tileSize * size.y
		)

		mwc = MainWindowConstructor(winSize)
		mwc.makeGame(self.update)
		mwc.makeVideo("graphics/RomanIJola_overlay_compressed.mp4")
		self.mainWindow = mwc.make()
		self.view = mwc.getGameView()

		self.controller = Controller()

	def setMap(self, m : Map):
		self.map = m
		self.controller.setMap(m)

	def show(self):
		self.initScene()
		self.mainWindow.getCurrentWindow().play()
		self.mainWindow.show()

	def update(self, obj = None):
		if type(obj) is KbdEvent:
			self.controller.keyEvent(obj)
		self.controller.step()
		self.view.updateScene()

	def initScene(self):
		self.addTile(self.map.background)
		self.addTile(self.map.mainHero)

	def addTile(self, t : Tile):
		self.view.scene().addItem(t)
