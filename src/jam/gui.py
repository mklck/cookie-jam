from .scene	import Scene
from .model	import Point, KbdEvent, Callback, CallbackData

from PyQt6.QtWidgets import QStackedWidget, QApplication, QMainWindow, QGraphicsView, QWidget, QVBoxLayout
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import QTimer

from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl

import sys

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

class Window(QWidget):
	def __init__(self, widget):
		super().__init__()
		self.layout = QVBoxLayout()
		self.layout.addWidget(widget)
		self.setLayout(self.layout)

class VideoWindow(Window):
	def __init__(self):
		self.video = QVideoWidget()
		self.started = False
		super().__init__(self.video)

	def loadVideo(self, path):
		self.media = QMediaPlayer()
		self.media.setSource(QUrl.fromLocalFile(path))
		self.media.setVideoOutput(self.video)
		self.media.mediaStatusChanged.connect(self.updateMediaStatus)

	def notYetStarted(self):
		return not self.started 

	def updateMediaStatus(self, status):
		self.mediaStatus = status

	def endOfMedia(self):
		return self.mediaStatus == QMediaPlayer.MediaStatus.EndOfMedia

	def play(self):
		self.started = True
		self.media.play()

	def stop(self):
		self.media.stop()

class GameWindow(Window):
	def __init__(self):
		self.initView()
		super().__init__(self.view)

	def initView(self):
		self.view = View()
		self.view.add('main', Scene())
		self.view.assign('main')

	def update(self):
		self.view.updateScene()

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

	def setCallback(self, cb : Callback):
		self.callback = cb

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

		cd = CallbackData(
			event=ev,
			window=self.getCurrentWindow()
		)
		self.callback(cd)

	def update(self):
		cd = CallbackData(
			event=None,
			window=self.getCurrentWindow()
		)
		self.callback(cd)

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

	def setCallback(self, cb : Callback):
		self.main.setCallback(cb)

	def makeGame(self):
		self.game = GameWindow()
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
