from .scene	import Scene
from .model	import Point

from PyQt6.QtWidgets import QStackedWidget, QApplication, QMainWindow, QGraphicsView, QWidget, QVBoxLayout
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import QTimer

from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl

import sys

class KbdEvent(str):
	pass

class View(QGraphicsView):
	def __init__(self):
		super().__init__()
		self.map = dict()
		self.assigned = None
	def getAssigned(self) -> str:
		return self.assigned
	def assign(self, name : str):
		self.setScene(self.map[name])
	def add(self, name : str, scene : Scene):
		self.map[name] = scene
	def remove(self, name : str):
		del self.meta[name]
	def updateScene(self):
		self.scene().updateAll()


class VideoWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.layout = QVBoxLayout()
		self.video = QVideoWidget()
		self.layout.addWidget(self.video)
		self.setLayout(self.layout)

	def loadVideo(self, path):
		self.media = QMediaPlayer()
		self.media.setSource(QUrl.fromLocalFile(path))
		self.media.setVideoOutput(self.video)

	def play(self):
		self.media.play()

	def stop(self):
		self.media.stop()

	def update(self, ev = None):
		pass

class GameWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initView()
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.view)
		self.setLayout(self.layout)

	def initView(self):
		self.view = View()
		self.view.add('main', Scene())
		self.view.assign('main')

	def setCallback(self, cb):
		self.callback = cb

	def update(self, ev = None):
		self.view.scene().update()
		self.callback(ev)

class MainWindow(QMainWindow):
	def __init__(self, size : Point):
		super().__init__()

		self.stack = QStackedWidget()

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.stack)

		self.container = QWidget()
		self.container.setLayout(self.layout)
		self.setCentralWidget(self.container)

		self.resize(size.x, size.y)
		self.grabKeyboard()
		self.windows = []
		self.timer = QTimer(self)

	def setQApp(self, qapp):
		self.app = qapp
	
	def addWindow(self, w : QWidget):
		self.windows.append(w)
		self.stack.addWidget(w)

	def switchWindow(self, window : QWidget):
		self.stack.setCurrentWidget(window)

	def getCurrentWindow(self):
		return self.stack.currentWidget()

	def keyPressEvent(self, ev):
		if type(ev) is QKeyEvent:
			ev = KbdEvent(ev.text())
		self.getCurrentWindow().update(ev)

	def update(self):
		self.getCurrentWindow().update()

	def show(self):
		self.timer.timeout.connect(self.update)
		self.timer.start(1000 // 25)
		super().show()
		sys.exit(self.app.exec())

class MainWindowConstructor:
	def __init__(self, size : Point):
		self.app = QApplication(sys.argv)
		self.size = size
		self.main = MainWindow(size)
		self.main.setQApp(self.app)

	def makeGame(self, cb):
		self.game = GameWindow()
		self.game.setCallback(cb)
		self.main.addWindow(self.game)

	def makeVideo(self, path):
		self.video = VideoWindow()
		self.video.loadVideo(path)
		self.main.addWindow(self.video)

	def make(self):
		self.main.switchWindow(self.video)
		return self.main

	def getGameView(self):
		return self.game.view
