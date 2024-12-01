from .scene	import Scene
from .model	import Point

from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QWidget, QVBoxLayout
from PyQt6.QtGui import QColor, QKeyEvent
from PyQt6.QtCore import QTimer, QRect
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
		if type(ev) is QKeyEvent:
			ev = KbdEvent(ev.text())
		self.callback(ev)

	def getScene(self):
		return self.view.scene()

	def show(self, callback):
		self.callback = callback
		self.timer.timeout.connect(self.update)
		self.timer.start(1000 // 25)
		self.window.show()
		sys.exit(self.app.exec())
