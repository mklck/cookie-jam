from .map		import Map
from .model		import Point, KbdEvent, Callback, CallbackData
from .tile		import Tile
from .gui		import MainWindowConstructor, VideoWindow, GameWindow
from .controller	import Controller
from .matches		import MenuWindow, MatchstickGame

import random

class CutScenes:
	def __init__(self):
		self.cutscenes = [
			'graphics/Scenes/scene1.mp4',
			'graphics/Scenes/scene2.mp4',
			'graphics/Scenes/scene3.mp4',
			'graphics/Scenes/scene4.mp4',
			'graphics/Scenes/scene5.mp4',
			'graphics/Scenes/scene6.mp4',
		]
		self.endings = [
			'graphics/Scenes/good_ending.mp4',
			'graphics/Scenes/bad_ending.mp4',
		]
		self.end = False
	def getCutscene(self):
		if len(self.cutscenes) == 0:
			return None
		p = random.choice(self.cutscenes)
		self.cutscenes.remove(p)
		return p
	def getEnding(self):
		self.end = True
		p = random.choice(self.endings)
		self.endings.remove(p)
		return p
	def any(self):
		return len(self.cutscenes) > 0

class Game:
	def __init__(self, size : Point, tileSize : int):
		Tile.setTileSize(tileSize)
		winSize = Point(
			tileSize * size.x,
			tileSize * size.y
		)

		self.cutscenes = CutScenes()
		self.end = False

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
		elif tp is MenuWindow:
			self.updateMenu(d)
		elif tp is MatchstickGame:
			self.updateMatch(d)
		elif tp is GameWindow:
			self.updateGame(d)

	def updateGame(self, d : CallbackData):
		if len(self.map.paper) == 0:
			if not self.cutscenes.end:
				self.mainWindow.playVideo(self.cutscenes.getEnding())
			else:
				exit()
		
		d.window.update()
		if type(d.event) is KbdEvent:
			self.controller.keyEvent(d.event)
		self.controller.step()
		if p := self.controller.steppedPaper:
			self.controller.clearPaper()
			self.initScene()
			self.mainWindow.switchWindow(self.mwc.menu)
			
	def updateMenu(self, d : CallbackData):
		if d.window.ready:
			r = d.window.getRiddle()
			self.mwc.makeMatchstick(r)
			self.mainWindow.switchWindow(self.mwc.match)
		

	def updateVideo(self, d : CallbackData):
		win, ev = d.window, d.event

		if win.notYetStarted():
			win.play()

		if type(ev) is KbdEvent or win.endOfMedia():
			win.stop()
			self.mainWindow.switchWindow(self.mwc.game)

	def updateMatch(self, d : CallbackData):
		if not d.window.passed:
			return

		print(self.cutscenes.cutscenes)
		p = self.cutscenes.getCutscene()
		self.mainWindow.playVideo(p)

	def initScene(self):
		self.clearScene()
		self.addTile(self.map.background)
		self.addTile(self.map.mainHero)
		for p in self.map.paper:
			self.addTile(p)

	def clearScene(self):
		self.view.scene().clear()

	def addTile(self, t : Tile):
		self.view.scene().addItem(t)
