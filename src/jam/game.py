from .map		import Map
from .model		import Point, KbdEvent, Callback, CallbackData
from .tile		import Tile
from .gui		import MainWindowConstructor, VideoWindow, GameWindow
from .controller	import Controller

class Game:
	def __init__(self, size : Point, tileSize : int):
		Tile.setTileSize(tileSize)
		winSize = Point(
			tileSize * size.x,
			tileSize * size.y
		)

		mwc = MainWindowConstructor(winSize)
		mwc.setCallback(self.update)
		mwc.makeGame()
		mwc.makeVideo("graphics/RomanIJola_overlay_compressed.mp4")

		self.mwc = mwc
		
		self.mainWindow = mwc.make()
		self.view = mwc.getGameView()

		self.controller = Controller()

	def setMap(self, m : Map):
		self.map = m
		self.controller.setMap(m)

	def show(self):
		self.initScene()
		self.mainWindow.show()

	def update(self, d : CallbackData):
		tp = type(d.window)
		if tp is VideoWindow:
			self.updateVideo(d)
		elif tp is GameWindow:
			d.window.update()
			if type(d.event) is KbdEvent:
				self.controller.keyEvent(d.event)
			self.controller.step()

	def updateVideo(self, d : CallbackData):
		win, ev = d.window, d.event

		if win.notYetStarted():
			win.play()

		if type(ev) is KbdEvent or win.endOfMedia():
			win.stop()
			self.mainWindow.switchWindow(self.mwc.game)

	def initScene(self):
		self.addTile(self.map.background)
		self.addTile(self.map.mainHero)

	def addTile(self, t : Tile):
		self.view.scene().addItem(t)
