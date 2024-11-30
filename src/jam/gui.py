from .tile import *

from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QWidget, QVBoxLayout
from PyQt6.QtGui import QColor, QKeyEvent
from PyQt6.QtCore import QTimer, QRect
import sys

class Scene(QGraphicsScene):
	def __init__(self):
		super().__init__()
		self.tiles = list()

	def addItem(self, t : Tile):
		self.tiles.append(t)
		qg = t.update()
		super().addItem(qg)

	def updateAll(self):
		for t in self.tiles:
			if not t.needUpdate():
				continue
			self.updateTile(t)

	def updateTile(self, t : Tile):
		self.removeItem(t.getGitem())
		self.addItem(t)


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


class Window(QWidget):
	def __init__(self, size : Point):
		self.app = QApplication(sys.argv)
		super().__init__()
		self.initView()
		self.initWindow(size)
		self.grabKeyboard()
		self.timer = QTimer(self)

	def initView(self):
		view = View()
		view.add('main', Scene())
		view.assign('main')
		self.view = view

	def initWindow(self, size : Point):
		self.window = QMainWindow()
		self.window.setCentralWidget(self.view)
		self.window.setWindowTitle("Map Drawer")
		self.window.resize(size.x, size.y)

	def update(self):
		self.view.scene().update()
		self.callback()

	def keyPressEvent(self, ev):
		self.callback(ev)

	def getScene(self):
		return self.view.scene()

	def show(self, callback):
		self.callback = callback
		self.timer.timeout.connect(self.update)
		self.timer.start(1000 // 25)
		self.window.show()
		sys.exit(self.app.exec())
